from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

BODY_TYPES = [
    ("sedan", "Sedan"),
    ("hatchback", "Hatchback"),
    ("liftback", "Liftback"),
    ("coupe", "Coupe"),
    ("crossover", "Crossover"),
    ("truck", "Truck"),
    ("wagon", "Wagon"),
]


class Model(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    body_type = models.CharField(max_length=20, choices=BODY_TYPES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "model"
        verbose_name_plural = "models"
