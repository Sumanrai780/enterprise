from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
