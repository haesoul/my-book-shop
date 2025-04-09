from django.urls import path

from .views import *

urlpatterns = [
    path('',MainPage.as_view(),name='home'),
    path('products/category/<slug:slug>/',CategorySelectedList.as_view(),name='category'),
    path('products/genre/<slug:slug>/',GenreSelectedList.as_view(),name='genre'),
    path('product-detail/<slug:slug>/',ProductDetailView.as_view(),name='product')

]
