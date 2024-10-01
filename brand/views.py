from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from brand.models import Brand
from brand.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by("id")
    serializer_class = BrandSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "name",
        "country",
    )

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]

        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]

        return super().get_permissions()
