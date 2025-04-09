from django.urls import path

from orders import views

app_name = 'order'
urlpatterns = [
    path('add-order/<slug:slug>/',views.AddOrderView.as_view(),name='create_order'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order-list/',views.OrderListView.as_view(),name='order-list')
]