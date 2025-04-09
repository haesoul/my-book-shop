from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import FormMixin

from orders.forms import *
from orders.models import *


class AddOrderView(LoginRequiredMixin,CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'orders/add-order.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Product.objects.get(slug=slug)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = self.get_object()
        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy('home')








class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        # Только заказы текущего пользователя
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавим связанные товары в заказе
        context['items'] = OrderItem.objects.filter(order=self.object)
        return context

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'


