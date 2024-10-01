from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from model.models import Model
from django_filters import rest_framework as filters

from model.serializers import ModelSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by("id")
    serializer_class = ModelSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "name",
        "year",
        "body_type",
    )

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]

        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]

        return super().get_permissions()
