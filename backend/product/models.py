from django.db import models


class ParameterStorage(models.Model):
    name = models.CharField(max_length=100)


class ValueStorage(models.Model):
    parameter = models.ForeignKey(ParameterStorage, on_delete=models.CASCADE)
    object = models.ForeignKey('BaseProduct', on_delete=models.CASCADE, null=True)
    value = models.TextField(blank=True)


class BaseProduct(models.Model):
    image = models.ImageField(blank=True, null=True)
    Model = models.TextField()
    ProductDescription = models.TextField()
    parameters = models.ForeignKey(ParameterStorage, related_name='ParameterStorage', on_delete=models.CASCADE)
    value = models.ForeignKey(ValueStorage, on_delete=models.CASCADE)
    price = models.IntegerField()
