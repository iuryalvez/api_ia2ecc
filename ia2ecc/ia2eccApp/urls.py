from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AnimalViewSet

# Criação do router
router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'animais', AnimalViewSet, basename='animais')

# Incluindo as URLs geradas pelo router
urlpatterns = [
    path('', include(router.urls)),
]
