from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import get_cart, add_to_cart, remove_from_cart

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'cart/product_detail.html', {'product': product})

def cart(request):
    cart = get_cart(request)
    cart_items = cart.items.all()
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})

def add_to_cart_view(request, pk):
    cart = add_to_cart(request, pk)
    return redirect('cart')

def remove_from_cart_view(request, pk):
    cart = remove_from_cart(request, pk)
    return redirect('cart')
def hx_menu_cart(request):
    cart = get_cart(request)  # Sử dụng hàm get_cart từ cart.py
    return render(request, 'cart/partials/menu_cart.html', {'cart': cart})