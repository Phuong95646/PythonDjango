from django import template

register = template.Library()

@register.filter
def sum_cart_items(items):
    total = sum(item.quantity * item.product.price for item in items)
    return total