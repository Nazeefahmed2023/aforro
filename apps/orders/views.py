
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.db.models import Prefetch
from apps.orders.models import Order, OrderItem, Inventory
from apps.orders.serializers import OrderSerializer, InventorySerializer
from apps.orders.tasks import async_send_order_confirmation

@api_view(['POST'])
def create_order(request):
    """
    Create a new order for a store.
    - Validates inventory for each requested product.
    - If any product is out of stock, order is REJECTED and no stock is deducted.
    - If all products are available, deduct stock and CONFIRM order.
    - Operation is atomic for consistency.
    """
    data = request.data
    store_id = data.get('store_id')
    items = data.get('items', [])
    with transaction.atomic():
        order = Order.objects.create(store_id=store_id, status='PENDING')
        insufficient = []
        for item in items:
            product_id = item['product_id']
            qty = int(item['quantity_requested'])
            try:
                inv = Inventory.objects.select_for_update().get(store_id=store_id, product_id=product_id)
                if inv.quantity < qty:
                    insufficient.append(product_id)
                else:
                    inv.quantity -= qty
                    inv.save()
            except Inventory.DoesNotExist:
                insufficient.append(product_id)
            OrderItem.objects.create(order=order, product_id=product_id, quantity_requested=qty)
        if insufficient:
            order.status = 'REJECTED'
            order.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
        order.status = 'CONFIRMED'
        order.save()
        # Send confirmation asynchronously
        async_send_order_confirmation.delay(order.id)
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_orders(request, store_id):
    """
    List all orders for a given store, sorted by newest first.
    Returns order ID, status, created_at, and total number of items.
    """
    orders = Order.objects.filter(store_id=store_id).prefetch_related('items').order_by('-created_at')
    data = [
        {
            'id': o.id,
            'status': o.status,
            'created_at': o.created_at,
            'total_items': o.items.count()
        } for o in orders
    ]
    return Response(data)


@api_view(['GET'])
def list_inventory(request, store_id):
    """
    List inventory for a store, sorted alphabetically by product title.
    Returns product title, price, category name, and quantity.
    """
    inventory = Inventory.objects.filter(store_id=store_id).select_related('product__category').order_by('product__title')
    data = [
        {
            'product_id': inv.product.id,
            'product_title': inv.product.title,
            'price': inv.product.price,
            'category_name': inv.product.category.name,
            'quantity': inv.quantity
        } for inv in inventory
    ]
    return Response(data)
