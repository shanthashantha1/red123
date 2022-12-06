from django.shortcuts import render
from rest_framework import viewsets
from .models import userProfile, Product, OrderItem, Order, Coupon
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer, CouponSerializer
from rest_framework import permissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [permissions.AllowAny]

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permissions_classes = [permissions.AllowAny]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permissions_classes = [permissions.AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = [permissions.AllowAny]

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount 
        return total       
    
         
