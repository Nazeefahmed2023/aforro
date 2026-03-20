

from django.urls import reverse
from rest_framework.test import APITestCase
from apps.products.models import Category, Product
from apps.stores.models import Store
from apps.orders.models import Inventory

class ProductSearchAPITest(APITestCase):
    """
    Test suite for the product search endpoint.
    Covers keyword search, stock filtering, and price range.
    """
    def setUp(self):
        # Create products and inventory for search tests
        cat = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(title='Laptop', price=1500, category=cat)
        self.product2 = Product.objects.create(title='Phone', price=800, category=cat)
        self.store = Store.objects.create(name='Store1', location='NY')
        Inventory.objects.create(store=self.store, product=self.product, quantity=10)
        Inventory.objects.create(store=self.store, product=self.product2, quantity=0)

    def test_search_by_title(self):
        """
        Should find product by title keyword.
        """
        url = reverse('search_products') + '?q=Laptop'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

    def test_search_in_stock(self):
        """
        Should only return products in stock for a store.
        """
        url = reverse('search_products') + f'?store_id={self.store.id}&in_stock=1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Laptop')

    def test_search_price_range(self):
        """
        Should filter products by price range.
        """
        url = reverse('search_products') + '?price_min=1000&price_max=2000'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)

# Additional tests for pagination, sorting, etc. can be added below.
