# serializers.py
from rest_framework import serializers
from ...models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['link_id', 'link', 'price']
