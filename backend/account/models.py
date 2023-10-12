from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

from chipBasket.models import ChipBasket


class User(EmailAbstractUser):
	# Custom fields
	adress = models.CharField(max_length=500)
	date_of_birth = models.DateField('Date of birth', null=True, blank=True)
	chips_basket = models.OneToOneField(ChipBasket, on_delete=models.CASCADE, null=True)
	# Required
	objects = EmailUserManager()

