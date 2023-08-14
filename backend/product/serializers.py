from rest_framework import serializers
from .models import ParameterStorage, BaseProduct, ValueStorage

class ParameterStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterStorage
        fields = '__all__'

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = '__all__'

class ValueStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueStorage
        fields = '__all__'
