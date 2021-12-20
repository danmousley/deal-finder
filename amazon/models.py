from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Item(models.Model):
    watchers = models.ManyToManyField(User, related_name = "followed_items")
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    url = models.URLField()
    last_checked = models.DateTimeField(auto_now_add=True)
    original_price = models.DecimalField(max_digits=12, decimal_places=2)
    current_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_deal = models.BooleanField(default=False)

