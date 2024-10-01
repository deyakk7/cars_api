from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from car.filters import CarFilter
from car.models import Car
from car.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(on_sale=True).order_by("id")
    serializer_class = CarSerializer

    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.OrderingFilter,
        rest_filters.SearchFilter,
    )
    filterset_class = CarFilter

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]

        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]

        return super().get_permissions()

    @action(detail=False, methods=["get"])
    def all(self, request):
        cars = Car.objects.all().order_by("id")
        for backend in list(self.filter_backends):
            cars = backend().filter_queryset(self.request, cars, self)
        serializer = self.get_serializer(cars, many=True)
        return Response(serializer.data)
