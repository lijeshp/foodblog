from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cartdetails', views.cartdetails,name='cartdetails'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
    path('minus/<int:product_id>/',views.minus_cart, name='minuscart'),
    path('delete/<int:product_id>/',views.delete_cart, name='deletecart')
]