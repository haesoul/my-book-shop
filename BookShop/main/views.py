from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import FormMixin

from cart.forms import CartItemForm
from cart.models import Cart, CartItem
from main.models import *


class MainPage(ListView):
    template_name = 'main/home.html'
    model = Product
    context_object_name = 'products'
    extra_context = {
        'categories':Category.objects.all()
    }


class CategorySelectedList(DetailView):
    model = Category
    template_name = 'main/selected-category.html'
    context_object_name = 'category'


class GenreSelectedList(DetailView):
    model = Genre
    template_name = 'main/selected-genre.html'
    context_object_name = 'genre'

class ProductDetailView(FormMixin,DetailView):
    model = Product
    template_name = 'main/product-detail.html'
    context_object_name = 'product'

    form_class = CartItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["initial"] = {"product": self.get_object()}
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            product = form.cleaned_data["product"]
            quantity = form.cleaned_data["quantity"]

            # Получаем корзину пользователя или создаём новую
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Добавляем товар в корзину (обновляем количество, если уже есть)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()

            return redirect("/")  # Перенаправляем в корзину

        return self.get(request, *args, **kwargs)


class AboutUs(TemplateView):
    pass




