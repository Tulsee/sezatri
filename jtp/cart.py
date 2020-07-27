
@api_view(['POST'])
def CartDetail(request):
    data = request.data
    dataId = data['id']
    response = {}
    user = get_object_or_404(User, id=dataId)
    customer = get_object_or_404(CustomerDetail, user=user.id)
    carts = Cart.objects.filter(customer=customer.id)
    serializer_context = {
        'request': request,
    }
    # for i in carts:
    #     productId = i.product.id
    #     product = Product.objects.get(id=productId)
    #     serializer1 = newProductSerializer(product, many=False)
    #     response.append(serializer1.data)

    #     print(product.thumbnail)
    serializer = CartSerializers(carts, many=True, context=serializer_context)
    # response['cart'] = serializer.data
    return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     id = self.kwargs.get(self.lookup_url_kwarg)
    #     queryset = Cart.objects.filter(customer=id)
    #     serializer_class = CartDetailSerializers(queryset, many=False)
    #     return Response(serializer_class.data)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     dataId = data['id']
    #     user = get_object_or_404(User, id=dataId)
    #     customer = get_object_or_404(CustomerDetail, user=user.id)
    #     cart = Cart.objects.filter(customer=customer.id)
    #     serializer = CartDetailSerializers(cart, many=True)
    #     return Response(serializer.data)


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    lookup_field = 'customer'

    def create(self, request, *args, **kwargs):
        # data = request.data
        dataCopy = request.data
        customerId = dataCopy['customer']
        user = get_object_or_404(User, id=customerId)
        print(user)
        customer, created = CustomerDetail.objects.get_or_create(user=user)
        productId = dataCopy['product']
        product = get_object_or_404(Product, id=productId)
        dataCopy['customer'] = customer.id
        print(product)
        try:
            query = get_object_or_404(Cart, customer=customer, product=product)
        except:
            query = False
        print(query)
        if(query):
            # dataCopy['quantity'] = dataCopy['quantity']+query.quantity
            # print(dataCopy)
            # serializer = CartSerializers(data=dataCopy)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            # else:
            #     return Response(serializer.errors)
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
        print(dataCopy)
        # customerId = dataCopy['customer']
        # user = get_object_or_404(User, id=customer)
        # print('user ==', user)
        # customer, created = CustomerDetail.objects.get_or_create(user=user.id)
        # productId = dataCopy['product']
        # customer = get_object_or_404(CustomerDetail, id=customerId)
        # product = get_object_or_404(Product, id=productId)
        # print('product ==', product)
        # dataCopy['customer'] = customer.id
        # query = get_object_or_404(Cart, customer=customer, product=product)
        dataCopy['quantity'] = dataCopy['quantity']+query.quantity
        serializer_class = CartSerializers(
            instance=query, data=dataCopy, partial=partial)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        print(dataCopy)
        return Response({"message": "created"}, status=status.HTTP_201_CREATED)
