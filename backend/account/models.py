from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

from chipBasket.models import ChipsBasket


class MyUser(EmailAbstractUser):
	# Custom fields
	date_of_birth = models.DateField('Date of birth', null=True, blank=True)
	chips_basket = models.OneToOneField(ChipsBasket, on_delete=models.CASCADE, null=True)
	# Required
	objects = EmailUserManager()