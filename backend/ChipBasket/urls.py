from django.urls import path
from .views import (
    ChipsBasketListCreateView,
    BasketItemListCreateView
)

urlpatterns = [
    path('chips-baskets/', ChipsBasketListCreateView.as_view()),
    path('basket-items/', BasketItemListCreateView.as_view())
]
