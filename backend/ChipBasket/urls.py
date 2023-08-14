from django.urls import path
from .views import (
    ChipsBasketListCreateView, ChipsBasketDetailView,
    BasketItemListCreateView, BasketItemDetailView,
)

urlpatterns = [
    path('chips-baskets/', ChipsBasketListCreateView.as_view(), name='chipsbasket-list'),
    path('chips-baskets/<int:pk>/', ChipsBasketDetailView.as_view(), name='chipsbasket-detail'),
    path('basket-items/', BasketItemListCreateView.as_view(), name='basketitem-list'),
    path('basket-items/<int:pk>/', BasketItemDetailView.as_view(), name='basketitem-detail'),
]
