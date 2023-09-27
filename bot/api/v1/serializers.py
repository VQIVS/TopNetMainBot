# serializers.py
from rest_framework import serializers
from ...models import Link, User

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['link_id', 'link', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email']
