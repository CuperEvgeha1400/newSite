from rest_framework import generics
from .models import ParameterStorage, BaseProduct, ValueStorage
from .serializers import ParameterStorageSerializer, BaseProductSerializer, ValueStorageSerializer


class ParameterStorageListCreateView(generics.ListAPIView):
    queryset = ParameterStorage.objects.all()
    serializer_class = ParameterStorageSerializer


class BaseProductListCreateView(generics.ListAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer


class ValueStorageListCreateView(generics.ListAPIView):
    queryset = ValueStorage.objects.all()
    serializer_class = ValueStorageSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ParameterStorageSerializer

    def get_queryset(self):
        queryset = BaseProduct.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

