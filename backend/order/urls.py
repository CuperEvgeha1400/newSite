from django.urls import path
from .views import (
    OrderListCreateView,
    OrderItemListCreateView
)

urlpatterns = [
    path('orders/', OrderListCreateView.as_view()),
    path('order-items/', OrderItemListCreateView.as_view())
]

