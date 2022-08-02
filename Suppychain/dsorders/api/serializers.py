from dataclasses import field, fields
from pyexpat import model
from threading import activeCount
from rest_framework import serializers
from dsorders.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id','username']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active and not user.is_staff:
            return user
        raise serializers.validationErrir("Incorrect Credentials")

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ("__all__")
class SalesmanSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = ("__all__")

class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("__all__")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = "__all__"

            
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        field ="__all__"
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderItems
        field = "__all__"