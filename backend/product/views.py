from rest_framework import generics
from .models import ParameterStorage, BaseProduct, ValueStorage
from .serializers import ParameterStorageSerializer, BaseProductSerializer, ValueStorageSerializer

class ParameterStorageListCreateView(generics.ListCreateAPIView):
    queryset = ParameterStorage.objects.all()
    serializer_class = ParameterStorageSerializer

class ParameterStorageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParameterStorage.objects.all()
    serializer_class = ParameterStorageSerializer

class BaseProductListCreateView(generics.ListCreateAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer

class BaseProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer

class ValueStorageListCreateView(generics.ListCreateAPIView):
    queryset = ValueStorage.objects.all()
    serializer_class = ValueStorageSerializer

class ValueStorageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValueStorage.objects.all()
    serializer_class = ValueStorageSerializer
