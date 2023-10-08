from django.urls import path
from .views import (
    ParameterStorageListCreateView,
    BaseProductListCreateView,
    ValueStorageListCreateView,
    ProductListView
)

urlpatterns = [
    path('parameter-storages/', ParameterStorageListCreateView.as_view()),
    path('base-products/', BaseProductListCreateView.as_view()),
    path('value-storages/', ValueStorageListCreateView.as_view()),
    path('products/', ProductListView.as_view(), name='product-list')
]
