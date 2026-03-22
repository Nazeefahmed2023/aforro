

from django.urls import reverse
from rest_framework.test import APITestCase
from apps.products.models import Category, Product
from apps.stores.models import Store
from apps.orders.models import Inventory


class ProductSearchAPITest(APITestCase):
    """
    Human-style test suite for the product search API.
    Each test covers a realistic user scenario.
    """

    def setUp(self):
        # Set up a store with two products: one in stock, one out of stock
        cat = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(title='Laptop', price=1500, category=cat)
        self.product2 = Product.objects.create(title='Phone', price=800, category=cat)
        self.store = Store.objects.create(name='Store1', location='NY')
        Inventory.objects.create(store=self.store, product=self.product, quantity=10)
        Inventory.objects.create(store=self.store, product=self.product2, quantity=0)

    def test_search_by_title(self):
        """
        Should return the correct product when searching by title keyword.
        """
        url = reverse('search_products') + '?q=Laptop'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Laptop')

    def test_search_in_stock(self):
        """
        Should only return products that are in stock for the given store.
        """
        url = reverse('search_products') + f'?store_id={self.store.id}&in_stock=1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Laptop')

    def test_search_price_range(self):
        """
        Should filter products by a given price range.
        """
        url = reverse('search_products') + '?price_min=1000&price_max=2000'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Laptop')

    def test_search_no_results(self):
        """
        Should return zero results if no products match the query.
        """
        url = reverse('search_products') + '?q=Nonexistent'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 0)

# Additional tests for pagination, sorting, etc. can be added below.
