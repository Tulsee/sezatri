from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from product.models import Product


class CustomerDetail(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    deviceId = models.CharField(max_length=48, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact = models.BigIntegerField(null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(
        CustomerDetail, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


class Cart(models.Model):
    customer = models.ForeignKey(
        CustomerDetail, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    checkout = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.product


class OrderItem(models.Model):
    customer = models.ForeignKey(
        CustomerDetail, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if(product):
            return self.product
        else:
            customer
