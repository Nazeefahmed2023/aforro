# get_valid_store_product.py
# Utility script to print a valid store-product pair and its inventory.
# Useful for debugging or demoing API endpoints that require valid IDs.

from apps.stores.models import Store
from apps.orders.models import Inventory

def main():
	"""
	Print the first store with at least one inventory record, along with product and quantity.
	"""
	store = Store.objects.first()
	if not store:
		print("No stores found in the database.")
		return

	inventory = Inventory.objects.filter(store=store).first()
	if not inventory:
		print(f"No inventory found for store: {store.name}")
		return

	product = inventory.product
	print(f"Store: {store.name} (ID: {store.id})")
	print(f"Product: {product.title} (ID: {product.id})")
	print(f"Quantity in stock: {inventory.quantity}")

if __name__ == "__main__":
	main()
