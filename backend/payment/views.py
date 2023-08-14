from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from account.models import MyUser
from ChipBasket.models import BasketItem
import stripe
import time
from product.models import BaseProduct
from .models import PromoCode
from django.core.exceptions import ValidationError
from django.utils import timezone


@login_required(login_url='login')
def product_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        promo_code = request.POST.get('promo_code')
        user_basket = BasketItem.objects.filter(user=request.user)
        basket_total = sum(item.subtotal() for item in user_basket)

        try:
            discount_amount = apply_promo_code(promo_code, basket_total)
            final_total = basket_total - discount_amount
        except ValidationError as e:
            final_total = basket_total
            error_message = str(e)

        line_items = []
        for basket_item in user_basket:
            product = basket_item.product
            item = {
                'name': product.Model,
                'price': int(product.price * (1 - discount_percentage / 100)),
                'quantity': basket_item.quantity,
            }
            line_items.append(item)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,  # Используем список элементов
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)

    return render(request, 'user_payment/product_page.html')


def apply_promo_code(promo_code, basket_total):
    try:
        promo = PromoCode.objects.get(code=promo_code)
        now = timezone.now()

        if promo.valid_from <= now <= promo.valid_until and promo.used_count < promo.max_usage:
            discount_amount = basket_total * promo.discount_percentage / 100
            return discount_amount
        else:
            raise ValidationError("Invalid or expired promo code.")
    except PromoCode.DoesNotExist:
        raise ValidationError("Invalid promo code.")




def increment_promo_usage(promo_code):
    promo = PromoCode.objects.get(code=promo_code)
    promo.increment_used_count()


@csrf_exempt
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
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        user_payment = MyUser.objects.get(stripe_checkout_id=session_id)

        # Увеличение счетчика использования промокода
        if user_payment.promo_code:
            increment_promo_usage(user_payment.promo_code)

        user_payment.payment_bool = True
        user_payment.save()
    return HttpResponse(status=200)