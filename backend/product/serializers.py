from rest_framework import serializers
from .models import ParameterName, BaseProduct, ParameterValue

class ParameterStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterName
        fields = '__all__'
        depth = 2

class BaseProductSerializer(serializers.ModelSerializer):
    parameters = serializers.SerializerMethodField()
    class Meta:
        model = BaseProduct
        fields = ('id', 'name', 'ProductDescription', 'price', 'parameters')

    def get_parameters(self, obj):
        # Создаем список параметров в формате ключ-значение (name-value)
        parameters = {}
        for param in obj.parameters.all():
            parameters[param.parameter.name] = param.value

        return parameters

class ValueStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterValue
        fields = '__all__'
        depth = 2
