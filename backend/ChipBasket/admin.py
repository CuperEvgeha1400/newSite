from django.contrib import admin

# Register your models here.
from .models import ChipsBasket,BasketItem

admin.site.register(ChipsBasket)
admin.site.register(BasketItem)
