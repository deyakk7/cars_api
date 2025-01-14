# Generated by Django 5.1.1 on 2024-10-01 23:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "year",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2024),
                        ]
                    ),
                ),
                (
                    "body_type",
                    models.CharField(
                        choices=[
                            ("sedan", "Sedan"),
                            ("hatchback", "Hatchback"),
                            ("liftback", "Liftback"),
                            ("coupe", "Coupe"),
                            ("crossover", "Crossover"),
                            ("truck", "Truck"),
                            ("wagon", "Wagon"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "model",
                "verbose_name_plural": "models",
                "ordering": ["name"],
            },
        ),
    ]
