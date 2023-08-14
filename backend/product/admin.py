from django.contrib import admin
from .models import BaseProduct, ParameterStorage,ValueStorage
# Register your models here.
admin.site.register(BaseProduct)
admin.site.register(ParameterStorage)
admin.site.register(ValueStorage)