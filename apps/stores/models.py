# --- Stores app models ---
from django.db import models

class Store(models.Model):
    """
    Represents a physical or online store.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        # Show the store name in admin and shell
        return self.name
