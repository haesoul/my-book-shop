from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import FormMixin

from orders.forms import *
from orders.models import *


class AddOrderView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'orders/add-order.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Product.objects.get(slug=slug)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        cart = Cart.objects.get(user=self.request.user)
        product = self.get_object()

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            messages.error(self.request, "Выбранный товар отсутствует в корзине.")
            return redirect('home')  # или на 'cart:view', если у тебя есть такой маршрут

        # Создаём OrderItem
        OrderItem.objects.create(
            order=self.object,
            product=product,
            quantity=cart_item.quantity,
            price=product.price
        )

        cart_item.delete()  # удаляем товар из корзины после заказа

        return response

    def get_success_url(self):
        return reverse_lazy('home')


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()  # <-- вот эта строка
        return context

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

