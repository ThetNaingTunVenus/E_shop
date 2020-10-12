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

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(categories=category_id)
        else:
            return Product.get_all_products()
        
