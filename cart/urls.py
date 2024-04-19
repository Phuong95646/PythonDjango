from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('hx-menu-cart/', views.hx_menu_cart, name='hx_menu_cart'),
]