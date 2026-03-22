

from django.urls import reverse
from rest_framework.test import APITestCase
from apps.products.models import Category, Product
from apps.stores.models import Store
from apps.orders.models import Inventory

class OrderAPITest(APITestCase):
    """
    Test suite for order creation logic.
    Covers both successful and failed order scenarios.
    """
    def setUp(self):
        # Create a category, product, store, and inventory for testing
        cat = Category.objects.create(name='Phones')
        self.product = Product.objects.create(title='iPhone', price=1000, category=cat)
        self.store = Store.objects.create(name='Store1', location='NY')
        Inventory.objects.create(store=self.store, product=self.product, quantity=5)

    def test_create_order_confirmed(self):
        """
        Should confirm order if enough stock is available.
        """
        url = reverse('create_order')
        data = {
            'store_id': self.store.id,
            'items': [{'product_id': self.product.id, 'quantity_requested': 2}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 'CONFIRMED')

    def test_create_order_rejected(self):
        """
        Should reject order if not enough stock is available.
        """
        url = reverse('create_order')
        data = {
            'store_id': self.store.id,
            'items': [{'product_id': self.product.id, 'quantity_requested': 10}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'REJECTED')

