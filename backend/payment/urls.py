from django.urls import path
from .views import create_checkout_session, stripe_webhook, CreateOrderViewRemote, PaypalToken

urlpatterns = [
    path('create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('CreateOrderViewRemote/', CreateOrderViewRemote.as_view())

]
