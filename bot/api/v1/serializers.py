# serializers.py
from rest_framework import serializers
from ...models import Link, User, Order, Email

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['link_id', 'link', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'primary_email', 'emails', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user_id', "username", 'link_id', 'email', 'status', 'quantity', 'created_at']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['address']







