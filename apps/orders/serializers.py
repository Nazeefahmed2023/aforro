
from rest_framework import serializers
from .models import Inventory, Order, OrderItem
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class InventorySerializer(serializers.ModelSerializer):
    """
    Serializes Inventory objects for API responses.
    """
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = Inventory
        fields = ['id', 'store', 'product', 'product_id', 'quantity']


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializes OrderItem objects for API responses.
    """
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_id', 'quantity_requested']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes Order objects, including nested items.
    """
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'store', 'status', 'created_at', 'items']

# Note: Add validation for business rules here if needed.
