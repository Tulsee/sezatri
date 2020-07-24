from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import store, CartViewSet

r = DefaultRouter()
r.register('view-set', CartViewSet)


urlpatterns = [
    path('', include(r.urls)),
    path("store/", store, name="store")
]
