from django.contrib import admin
from .models import userProfile, Product, Coupon, Order, OrderItem
# Register your models here.

admin.site.register(userProfile)
admin.site.register(Product)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
