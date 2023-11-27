from rest_framework import serializers
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        depth = 2
        fields = ('id', 'content', 'rating', 'product', 'author')