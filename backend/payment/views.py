import uuid

from django.http import JsonResponse
from paypal.standard.forms import PayPalPaymentsForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.utils import timezone
from .models import UserPayment
from chipBasket.models import BasketItem
from product.models import BaseProduct
from promocode.models import PromoCode
import stripe
import time
from paypalrestsdk import Payment
from account.models import MyUser
from django.shortcuts import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings

def increment_promo_usage(promo_code):
    promo = PromoCode.objects.get(code=promo_code)
    promo.increment_used_count()


def apply_promo_code(promo_code, basket_items):
    price = 0
    for item in basket_items:
        price += basket_items[item].product.price * basket_items[item].quantity


    try:
        promo = PromoCode.objects.get(code=promo_code)
        now = timezone.now()

        if promo.valid_from <= now <= promo.valid_until and promo.used_count < promo.max_usage:
            discount_amount = price * promo.discount_percentage / 100
            return discount_amount
        else:
            raise ValidationError("Invalid or expired promo code.")
    except PromoCode.DoesNotExist:
        raise ValidationError("Invalid promo code.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):

    promocode = request.data.get("promocode")

    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    user_basket = request.user.chips_basket

    if user_basket:
        basket_items = BasketItem.objects.filter(basket=user_basket)

    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    line_items = []

    for item in range(len(basket_items)):
        name = basket_items[item].product
        currency = 'czk'
        price = basket_items[item].product.price
        item = {
            'price_data':{
                'currency' : currency,
                'unit_amount':price*100,
                'product_data':{
                    'name':name
                }
            },
            'quantity': basket_items[item].quantity,
        }
        line_items.append(item)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        allow_promotion_codes= True,
        customer_creation='always',
        success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
    )

    return Response({'url': checkout_session.url}, status=status.HTTP_200_OK)


# Define apply_promo_code, payment_successful, payment_cancelled, increment_promo_usage functions here

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stripe_webhook(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except ValueError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except stripe.error.SignatureVerificationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        user_payment = MyUser.objects.get(stripe_checkout_id=session_id)

        if user_payment.promo_code:
            increment_promo_usage(user_payment.promo_code)

        user_payment.payment_bool = True
        user_payment.save()

    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CheckOut(request):
    user_basket = request.user.chips_basket

    if user_basket:
        basket_items = BasketItem.objects.filter(basket=user_basket)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    line_items = []

    host = request.get_host()

    for item in basket_items:
        price = item.product.price
        name = item.product
        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': price,
            'item_name': name,
            'invoice': uuid.uuid4(),
            'currency_code': 'czk',
            'notify_url': f"http://{host}{reverse('paypal-ipn')}",
            'return_url': f"http://{host}{reverse('payment-success')}",
            'cancel_url': f"http://{host}{reverse('payment-failed')}",
        }
        line_items.append(paypal_checkout)

    # Calculate the total price here based on line_items
    total_price = sum(float(item['amount']) for item in line_items)

    # Generate a ready-made PayPal payment link
    paypal_url = f"https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_xclick&charset=utf-8&currency_code=czk&no_shipping=1&business={settings.PAYPAL_RECEIVER_EMAIL}&amount={total_price}&item_name=Your item name&invoice={uuid.uuid4()}&notify_url=http://{host}{reverse('paypal-ipn')}&return=http://{host}{reverse('payment-success')}&cancel_return=http://{host}{reverse('payment-failed')}"
    # Возвращаем готовую ссылку на оплату PayPal в виде JSON-ответа
        
    return JsonResponse({'paypal_payment_link': paypal_url})

def PaymentSuccessful(request):
    return Response(request, status=status.HTTP_200_OK)

def paymentFailed(request):
    return Response(request, status=status.HTTP_400_BAD_REQUEST)