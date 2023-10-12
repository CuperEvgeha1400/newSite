from django.contrib import admin
from .models import BaseProduct, ParameterName,ParameterValue
# Register your models here.



admin.site.register(BaseProduct)
admin.site.register(ParameterName)
admin.site.register(ParameterValue)