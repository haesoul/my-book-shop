from django import forms

from cart.models import *
from .models import *



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'status']  # Не включаем 'user', так как он будет автоматически передаваться



class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # При изменении товара, автоматически подставляем цену из модели Product
            if self.instance and self.instance.product:
                self.fields['price'].initial = self.instance.product.price

        def save(self, commit=True):
            instance = super().save(commit=False)
            if instance.product:
                instance.price = instance.product.price  # Подставляем цену из модели Product
            if commit:
                instance.save()
            return instance