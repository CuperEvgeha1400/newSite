from rest_framework import serializers
from .models import ChipsBasket, BasketItem
from product.models import BaseProduct

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    product = BaseProductSerializer()

    class Meta:
        model = BasketItem
        fields = '__all__'

class ChipsBasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True, read_only=True)

    class Meta:
        model = ChipsBasket
        fields = '__all__'
