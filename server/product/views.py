from rest_framework import status, viewsets, filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .serializers import ProductSerializer, newProductSerializer


from .models import Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', ]
    # search_fields = ('name', 'category', 'price')


class NewProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.order_by(
        '-listed_date').filter(is_published=True)
    queryset = queryset[:4]
    serializer_class = newProductSerializer

    def get(self, request):
        if request.user.is_authenticated:
            print("USER", request.user)
        else:
            print("USER not authenticated")


class featureProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.order_by(
        '-views').filter(is_published=True)
    queryset = queryset[:4]
    serializer_class = newProductSerializer


# class featureProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.order_by(
#         '-listed_date').filter(is_published=True)
#     serializer_class = newProductSerializer

    # def get_queryset(self):
    #     return Product.objects.all()

    # def get(self, request, format=None):
    #     # response = {}
    #     # response['new_product'] = NewProductViewSet.as_view()(request).data
    #     data = featureViewSet.as_view(request).data

    #     return Response({'data': data})
