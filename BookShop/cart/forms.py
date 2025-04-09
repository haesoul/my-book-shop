from django import forms

from cart.models import *




class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product','quantity']
        widgets = {
            'product': forms.HiddenInput(attrs={'class': 'form-control'}),

            'quantity': forms.NumberInput(attrs={'class': 'form-control','min': '1',}),
        }

        labels = {
            'product': 'Товар',
            'quantity': 'Количество',
        }