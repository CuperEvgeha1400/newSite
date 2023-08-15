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
