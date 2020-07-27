from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartDetailViewSet

r = DefaultRouter()
r.register('view-set', CartViewSet, basename='cart')
# r.register('cart-detail/<int:id>', CartDetailViewSet, basename='cart-detail')


urlpatterns = [
    path('', include(r.urls)),
    path('cartdetial/<int:id>', CartDetailViewSet.as_view(), name='detail-cart')
    # path("store/", store, name="store")
]
