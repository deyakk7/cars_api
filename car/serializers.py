from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = "__all__"
