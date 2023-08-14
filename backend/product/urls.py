from django.urls import path
from .views import (
    ParameterStorageListCreateView, ParameterStorageDetailView,
    BaseProductListCreateView, BaseProductDetailView,
    ValueStorageListCreateView, ValueStorageDetailView,
)

urlpatterns = [
    path('parameter-storages/', ParameterStorageListCreateView.as_view(), name='parameterstorage-list'),
    path('parameter-storages/<int:pk>/', ParameterStorageDetailView.as_view(), name='parameterstorage-detail'),
    path('base-products/', BaseProductListCreateView.as_view(), name='baseproduct-list'),
    path('base-products/<int:pk>/', BaseProductDetailView.as_view(), name='baseproduct-detail'),
    path('value-storages/', ValueStorageListCreateView.as_view(), name='valuestorage-list'),
    path('value-storages/<int:pk>/', ValueStorageDetailView.as_view(), name='valuestorage-detail'),
]
