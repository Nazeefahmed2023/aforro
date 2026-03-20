# --- Products app models ---
from django.db import models

class Category(models.Model):
    """
    Represents a product category (e.g., Electronics, Clothing).
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # Show the category name in admin and shell
        return self.name


class Product(models.Model):
    """
    Represents a product with title, description, price, and category.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        # Show the product title in admin and shell
        return self.title
