from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models


class MapPin(models.Model):
    CATEGORY_CHOICES = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    contact_person = models.CharField(max_length=50)
    assigned_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name
