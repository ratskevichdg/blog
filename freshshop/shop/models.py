from django.db import models
from random import randrange
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey


# class Item(models.Model):
#     def save_to(self, filename):
#         file_type = filename.split(".")[-1]
#         file_name = ".".join(["{}/{}", file_type])
#         return file_name.format(self.name, randrange(1000000, 9999999))

#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to=save_to)

#     class Meta:
#         db_table = "items"


class Product(models.Model):
    def save_to(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}", file_type])
        return file_name.format(self.item_name, randrange(1000000, 9999999))

    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=save_to)
    quantity = models.IntegerField(null=True)

class Catalogue(models.Model):
    product_id = ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    order_quantity = models.IntegerField()
    product_id = ForeignKey('Product', on_delete=models.CASCADE)
    deal_id = ForeignKey('Deal', on_delete=CASCADE)

class Deal(models.Model):
    client_id = models.IntegerField() # надо подумать как связать с БД пользователей
    deal_date = models.DateField()
    delivery_date = models.DateTimeField()
