from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', views.RegisterUserViewSet)
# router.register('login', TokenObtainPairView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    # path('register/', views.RegisterUser, name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
