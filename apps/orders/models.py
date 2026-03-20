# --- Orders app models ---
from django.db import models
from apps.stores.models import Store
from apps.products.models import Product

class Inventory(models.Model):
    """
    Represents inventory for a product in a store.
    Each store-product pair is unique.
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='inventories')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('store', 'product')

    def __str__(self):
        # Show store and product in admin and shell
        return f"{self.store.name} - {self.product.title}"


class Order(models.Model):
    """
    Represents an order placed at a store.
    Status can be PENDING, CONFIRMED, or REJECTED.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('REJECTED', 'Rejected'),
    ]
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Show order ID and status in admin and shell
        return f"Order {self.id} - {self.status}"


class OrderItem(models.Model):
    """
    Represents an item in an order, referencing a product and requested quantity.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntegerField()

    def __str__(self):
        # Show product and quantity in admin and shell
        return f"{self.product.title} x {self.quantity_requested}"
