from rest_framework import serializers
from .models import Order, OrderItem, OrderStatus

class OrderStatusSerializer(serializers.Serializer):
    value = serializers.CharField(max_length=50)
    display_name = serializers.CharField(max_length=50)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 2


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
