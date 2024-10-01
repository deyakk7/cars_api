from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.UserViewSet)

urlpatterns = [
    path("create/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="register"),
] + router.urls
