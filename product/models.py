from django.db import models

class Weight(models.Model):
    weight_range = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.weight_range} / {self.price}"


class Product(models.Model):
    PRASUM_CHOICES = (
        ("pending", "PENDING"),
        ("delivered", "DELIVERED"),
        ("return", "RETURN")
    )
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices= PRASUM_CHOICES)
    remarks = models.TextField(null=True, blank=True)

def __str__(self):
    return self.name

def save(self, *args, **Kwargs):
    if self.pk is None:
        self.status = "pending"
    super().save(*args, **kwargs)