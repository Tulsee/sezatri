from rest_framework import serializers
from .models import Cart


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    # def save(self):
    #     cart = Cart(
    #         # customer=self.validated_data['customer'],
    #         product=self.validated_data['product'],
    #         # quantity=self.validated_data['quantity'],
    #         # total_price=self.validated_data['total_price'],
    #         # checkout=self.validated_data['checkout']
    #     )
    #     cart.save()
    #     return cart
