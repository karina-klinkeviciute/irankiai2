from django.db import models
from user.models import User


class Category(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category


class Tool(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
