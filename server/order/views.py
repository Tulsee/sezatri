from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


from product.models import Product
from .models import CustomerDetail, Order, OrderItem, Cart
from user.models import User


from .serializers import CartSerializers


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    lookup_field = 'customer'

    def create(self, request, *args, **kwargs):
        # data = request.data
        dataCopy = request.data
        customer = dataCopy['customer']
        user = get_object_or_404(User, id=customer)
        customer, created = CustomerDetail.objects.get_or_create(user=user)
        dataCopy['customer'] = customer.id
        serializer = CartSerializers(data=dataCopy)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        # if(created):
        #     dataCopy['customer'] = created.id
        #     serializer = CartSerializers(data=dataCopy)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     else:
        #         return Response(serializer.errors)
        # else:
        #     dataCopy['customer'] = customer.id
        #     serializer = CartSerializers(data=dataCopy)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     else:
        #         return Response(serializer.errors)
        # if(created):
        #     return Response({'message': created})
        #     dataCopy['customer'] = created.id
        #     serializer = CartSerializers(data=dataCopy)
        #     print('data', serializer.data)
        #     if serializer.is_valid():
        #         print('data', serializer.data)
        #         serializer.save()
        #         return Response(serializer.data)
        #     else:
        #         return Response(serializer.errors)
        # else:
        #     dataCopy['customer'] = customer.id
        #     serializer = CartSerializers(data=dataCopy)
        #     print('data', serializer.data)
        #     if serializer.is_valid():
        #         print('data', serializer.data)
        #         serializer.save()
        #         return Response(serializer.data)
        #     else:
        #         return Response(serializer.errors)

        return Response({"message": "created"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def store(request):
    if request.method == 'POST':
        cart = request.data
        # product_id = cart['product']
        # cart['product'] = get_object_or_404(Product, id=product_id)
        serializer = CartSerializers(data=cart)
        if serializer.is_valid():
            cart = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # data['product'] = get_object_or_404(Product, id=product_id)


# class Store(APIView):
#     cart = request.data
#     user_id = cart['user']
#     product_id = cart['product_id']
#     quantity = cart['quantity']

# { "quantity": 1, "total_price": 1000,"checkout": false,"customer": 1,"product": 4}
