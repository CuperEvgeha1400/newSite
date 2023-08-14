from django.db import models
from account.models import MyUser
from product.models import BaseProduct
from enum import Enum
from promocode.models import PromoCode


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)

class OrderStatus(Enum):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'

    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(BaseProduct, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices(),
        default=OrderStatus.PENDING.value,
    )

    class Meta:
        verbose_name_plural = 'OrderItems'
