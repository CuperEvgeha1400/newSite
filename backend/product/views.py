from .filters import CombinedFilter
from django_filters import rest_framework as filters
from rest_framework import generics
from .models import ParameterName, BaseProduct, ParameterValue, BaseProductImage
from .serializers import ParameterStorageSerializer, BaseProductSerializer, ValueStorageSerializer


class ParameterStorageListCreateView(generics.ListAPIView):
    queryset = ParameterName.objects.all()
    serializer_class = ParameterStorageSerializer


class BaseProductListCreateView(generics.ListAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer


class ValueStorageListCreateView(generics.ListAPIView):
    queryset = ParameterValue.objects.all()
    serializer_class = ValueStorageSerializer


class BaseProductListView(generics.ListAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CombinedFilter

    def get_queryset(self):
        base_product_id = self.kwargs['base_product_id']
        return BaseProductImage.objects.filter(base_product_id=base_product_id)

class BaseProductRetrieveView(generics.RetrieveAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer
