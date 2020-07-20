from rest_framework import status, viewsets, filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer


from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', ]
    # search_fields = ('name', 'category', 'price')
