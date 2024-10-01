from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="CARS API",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("cars/", include("car.urls")),
    path("models/", include("model.urls")),
    path("brands/", include("brand.urls")),
    path("user/", include("users.urls")),
    # Swagger
    path(
        "index/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
