from django.db import models
from django.utils import timezone

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    max_usage = models.PositiveIntegerField(null=True)
    used_count = models.PositiveIntegerField(default=0)  # Добавили счетчик использований

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("valid_from")
        end_date = cleaned_data.get("valid_until")
        if end_date < start_date:
            raise PromoCode.ValidationError("End date should be greater than start date.")

    def increment_used_count(self):
        self.used_count += 1
        self.save()

    def __str__(self):
        return self.code
