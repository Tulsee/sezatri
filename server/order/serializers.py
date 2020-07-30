from rest_framework import serializers
from .models import Cart
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'thumbnail']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer', 'product', 'quantity', 'checkout']


class CartDetailSerializers(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ['customer', 'product', 'quantity', 'checkout']
