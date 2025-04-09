from django.db import models

from main.models import *
from users.models import *


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Один пользователь — одна корзина
    products = models.ManyToManyField(Product, through="CartItem")  # Связь через промежуточную таблицу



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product',verbose_name='товар')
    quantity = models.PositiveIntegerField(default=1,verbose_name='количество')  # Количество товаров в корзине

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"