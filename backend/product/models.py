from django.db import models


class ParameterStorage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ValueStorage(models.Model):
    parameter = models.ForeignKey(ParameterStorage, on_delete=models.CASCADE)
    value = models.TextField(blank=True)

    def __str__(self):
        return self.value


class BaseProduct(models.Model):
    image = models.ImageField(blank=True, null=True)
    Model = models.TextField()
    ProductDescription = models.TextField()
    parameters = models.ManyToManyField(ParameterStorage, related_name='base_products')
    price = models.IntegerField()

    def __str__(self):
        return self.Model