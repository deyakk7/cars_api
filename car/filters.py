from django_filters import rest_framework as filters
from .models import Car


class CarFilter(filters.FilterSet):
    year_min = filters.NumberFilter(field_name="model__year", lookup_expr="gte")
    year_max = filters.NumberFilter(field_name="model__year", lookup_expr="lte")
    mileage_min = filters.NumberFilter(field_name="mileage", lookup_expr="gte")
    mileage_max = filters.NumberFilter(field_name="mileage", lookup_expr="lte")
    price_min = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = filters.NumberFilter(field_name="price", lookup_expr="lte")
    brand = filters.CharFilter(field_name="brand__name", lookup_expr="icontains")
    model = filters.CharFilter(field_name="model__name", lookup_expr="icontains")
    on_sale = filters.BooleanFilter(field_name="on_sale")

    class Meta:
        model = Car
        fields = [
            "exterior_color",
            "interior_color",
            "fuel_type",
            "transmission",
            "engine",
        ]
