from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    pprice = models.IntegerField(default=0)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
