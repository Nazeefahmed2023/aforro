
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializes Category objects for API responses.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes Product objects, including nested category info.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'category_id']

# Note: Add custom validation here if business rules require it.
