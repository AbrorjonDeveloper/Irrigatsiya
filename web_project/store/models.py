from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
