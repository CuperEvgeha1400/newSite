from django.db import models
from django.utils import timezone

from product.models import BaseProduct

class ChipsBasket(models.Model):
    date = models.DateField(default=timezone.now)


class BasketItem(models.Model):
    basket = models.ForeignKey(ChipsBasket, on_delete=models.CASCADE)
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
