from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, Product

def get_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return cart

def remove_from_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return cart