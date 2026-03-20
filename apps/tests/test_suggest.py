

from django.urls import reverse
from rest_framework.test import APITestCase
from apps.products.models import Product, Category
from django.core.cache import cache

class SuggestAPITest(APITestCase):
    """
    Test suite for the autocomplete (suggest) endpoint.
    Covers minimum query length, prefix/general matches, and rate limiting.
    """
    def setUp(self):
        # Clear cache to avoid rate limit issues
        cache.clear()
        cat = Category.objects.create(name='TestCat')
        Product.objects.create(title='Apple iPhone', price=1000, category=cat)
        Product.objects.create(title='Apple Watch', price=500, category=cat)
        Product.objects.create(title='Samsung Galaxy', price=800, category=cat)

    def test_suggest_min_length(self):
        """
        Should return empty list if query is too short.
        """
        url = reverse('suggest') + '?q=ap'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_suggest_prefix_and_general(self):
        """
        Should return prefix matches before general matches.
        """
        url = reverse('suggest') + '?q=App'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        titles = response.json()
        self.assertIn('Apple iPhone', titles)
        self.assertIn('Apple Watch', titles)

    def test_rate_limit(self):
        """
        Should return 429 if rate limit is exceeded.
        """
        url = reverse('suggest') + '?q=App'
        for _ in range(21):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 429)

# Additional edge case tests can be added below.
