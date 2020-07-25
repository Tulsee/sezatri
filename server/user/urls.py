from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_jwt.views import obtain_jwt_token

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', views.RegisterUserViewSet, basename="register")
router.register('me', views.GetAuthUserViewSet, basename="me")


urlpatterns = [
    path('', include(router.urls)),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', obtain_jwt_token, name='token_obtain_pair'),
    path('getuser/', views.GetUser, name="authUser")
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
