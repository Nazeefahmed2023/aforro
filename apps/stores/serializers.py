
from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    """
    Serializes Store objects for API responses.
    """
    class Meta:
        model = Store
        fields = ['id', 'name', 'location']
