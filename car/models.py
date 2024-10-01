from django.core.validators import (
    MinValueValidator,
    MaxLengthValidator,
    MaxValueValidator,
)
from django.db import models

from brand.models import Brand
from model.models import Model

FUEL_TYPES = [
    ("gasoline", "Gasoline"),
    ("diesel", "Diesel"),
    ("electric", "Electric"),
    ("hybrid", "Hybrid"),
]


TRANSMISSION_TYPES = [
    ("manual", "Manual"),
    ("automatic", "Automatic"),
]


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="cars")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    mileage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999999)]
    )
    exterior_color = models.CharField(max_length=20)
    interior_color = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_TYPES)
    engine = models.CharField(max_length=20)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} -- {self.model}"

    class Meta:
        ordering = ["price"]
        verbose_name = "car"
        verbose_name_plural = "cars"
