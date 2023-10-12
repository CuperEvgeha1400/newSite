from django.urls import path
from .views import create_checkout_session, stripe_webhook, CreateOrderViewRemote, check_and_create_order

urlpatterns = [
    path('create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('CreateOrderViewRemote/', CreateOrderViewRemote.as_view()),
    path('check_and_create_order/', check_and_create_order, name='check_and_create_order'),

]
