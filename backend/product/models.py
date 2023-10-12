from django.db import models


class ParameterName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class ParameterValue(models.Model):
    parameter = models.ForeignKey(ParameterName, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return f"{self.value} {self.parameter.name}"


class BaseProduct(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    ProductDescription = models.TextField()
    parameters = models.ManyToManyField(ParameterValue, related_name='base_products')
    price = models.IntegerField()

    def __str__(self):
        return self.name