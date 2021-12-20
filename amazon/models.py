from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Item(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name = "followed_items")
    name = models.CharField(max_length=64)
    title = name = models.CharField(max_length=64)
    original_price = models.DecimalField(max_digits=12, decimal_places=2)
    current_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_deal = models.BooleanField(default=False)

