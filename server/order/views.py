from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView


from product.models import Product
from .models import CustomerDetail, Order, OrderItem, Cart
from product.models import Product
from user.models import User


from .serializers import CartSerializers, CartDetailSerializers
from product.serializers import newProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    lookup_field = 'customer'

    def create(self, request, *args, **kwargs):
        dataCopy = request.data
        customerId = dataCopy['customer']
        user = get_object_or_404(User, id=customerId)
        # print(user)
        customer, created = CustomerDetail.objects.get_or_create(user=user)
        productId = dataCopy['product']
        product = get_object_or_404(Product, id=productId)
        dataCopy['customer'] = customer.id
        # print(product)
        try:
            query = get_object_or_404(Cart, customer=customer, product=product)
        except:
            query = False
        # print(query)
        if(query):
            self.quantityUpdate(request, query)
            return Response({"message": "update"}, status=status.HTTP_201_CREATED)
        else:
            serializer = CartSerializers(data=dataCopy)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
            return Response({"message": "created"}, status=status.HTTP_201_CREATED)

    def quantityUpdate(self, request, query, *args, **kwargs):
        dataCopy = request.data
        partial = kwargs.pop('partial', False)
        # print(dataCopy)
        dataCopy['quantity'] = dataCopy['quantity']+query.quantity
        serializer_class = CartSerializers(
            instance=query, data=dataCopy, partial=partial)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        # print(dataCopy)
        return Response({"message": "created"}, status=status.HTTP_201_CREATED)


class CartDetailViewSet(ListAPIView):
    serializer_class = CartDetailSerializers
    lookup_url_kwarg = "id"

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        user = get_object_or_404(User, id=id)
        customer = get_object_or_404(CustomerDetail, user=user.id)
        queryset = Cart.objects.filter(customer=customer.id)
        return queryset

    @classmethod
    def get_extra_actions(self):
        return Response('TEST')
