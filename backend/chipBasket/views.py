from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .models import ChipsBasket, BasketItem
from .serializers import ChipsBasketSerializer, BasketItemSerializer


@permission_classes([AllowAny])
class ChipsBasketListCreateView(generics.ListAPIView):
    queryset = ChipsBasket.objects.all()
    serializer_class = ChipsBasketSerializer


@permission_classes([AllowAny])
class BasketItemListCreateView(generics.ListAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
