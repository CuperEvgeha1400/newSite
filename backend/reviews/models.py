from django.db import models
from product.models import BaseProduct
from account.models import MyUser

class Review(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE, related_name='reviews')