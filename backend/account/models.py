from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

from chipBasket.models import ChipBasket


class User(EmailAbstractUser):
	# Custom fields
	adress = models.CharField(max_length=500)
	first_name = models.CharField(max_length=30, null=True, blank=True)
	last_name = models.CharField(max_length=30, null=True, blank=True)
	country = models.CharField(max_length=30, null=True, blank=True)
	region = models.CharField(max_length=30, null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	phone = models.CharField(max_length=30, null=True, blank=True)
	chips_basket = models.OneToOneField(ChipBasket, on_delete=models.CASCADE, null=True)
	# Required
	objects = EmailUserManager()

