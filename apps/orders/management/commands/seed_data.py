from django.core.management.base import BaseCommand
from apps.products.models import Category, Product
from apps.stores.models import Store
from apps.orders.models import Inventory
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy data.'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Categories
        categories = [Category.objects.create(name=fake.unique.word()) for _ in range(12)]
        # Products
        products = [Product.objects.create(
            title=fake.unique.sentence(nb_words=3),
            description=fake.text(max_nb_chars=100),
            price=round(random.uniform(5, 500), 2),
            category=random.choice(categories)
        ) for _ in range(1200)]
        # Stores
        stores = [Store.objects.create(
            name=fake.company(),
            location=fake.city()
        ) for _ in range(25)]
        # Inventory
        for store in stores:
            inv_products = random.sample(products, 350)
            for product in inv_products:
                Inventory.objects.create(
                    store=store,
                    product=product,
                    quantity=random.randint(1, 100)
                )
        self.stdout.write(self.style.SUCCESS('Seed data created.'))
