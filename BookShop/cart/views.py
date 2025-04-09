from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from cart.forms import *
from cart.models import *
from orders.models import *


class CartView(FormMixin, ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'cart'
    form_class = CartItemForm
    success_url = reverse_lazy('cart:cart')

    def dispatch(self, request, *args, **kwargs):
        # Проверка, что пользователь авторизован
        if not request.user.is_authenticated:
            return redirect('login')  # Перенаправить на страницу входа, если пользователь не авторизован
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Получаем все товары в корзине текущего пользователя
        return CartItem.objects.filter(cart__user=self.request.user)

    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('delete_item_id')

        if item_id:
            item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
            item.delete()

        # Если запрос на оформление заказа
        if request.POST.get('place_order'):
            return self.place_order(request)

        return redirect(self.get_success_url())

    def place_order(self, request):
        # Получаем корзину текущего пользователя
        cart_items = CartItem.objects.filter(cart__user=request.user)

        # Создаем заказ
        order = Order.objects.create(user=request.user, status='pending')

        # Добавляем товары из корзины в заказ
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price  # Цена товара из модели Product
            )

        # После оформления заказа, очищаем корзину
        cart_items.delete()

        # Перенаправляем пользователя на страницу с подтверждением заказа или страницу заказа
        return redirect('order:order_detail', pk=order.id)

