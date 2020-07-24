from django.contrib import admin
from .models import Cart, CustomerDetail, Order, OrderItem


admin.site.register(Cart)
admin.site.register(CustomerDetail)
admin.site.register(Order)
admin.site.register(OrderItem)
