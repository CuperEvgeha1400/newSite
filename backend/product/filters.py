import django_filters
from .models import BaseProduct
from rest_framework import filters


class BaseProductFilter(django_filters.FilterSet):
    class Meta:
        model = BaseProduct
        fields = []

    @classmethod
    def filter_for_field(cls, f, field_name, lookup_expr='exact'):
        filter_class, params = super().filter_for_field(f, field_name, lookup_expr)
        if f.is_relation and hasattr(f.related_model, 'baseproduct'):
            return BaseProductFilter, params
        return filter_class, params
