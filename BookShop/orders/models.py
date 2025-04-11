from django.db import models

from main.models import *
from users.models import *


class Location(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey('Location',on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    status = models.CharField(max_length=20, default='pending')  # pending, paid, shipped и т.п.

    def __str__(self):
        return f"Order #{self.id} by {self.user}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)










