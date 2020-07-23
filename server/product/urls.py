from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('all', views.ProductViewSet)
router.register('newproduct', views.NewProductViewSet, basename="newproduct")
router.register('featureproduct', views.featureProductViewSet,
                basename="featureproduct")


urlpatterns = [
    path('', include(router.urls))
]
