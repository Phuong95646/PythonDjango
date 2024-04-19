from blog.models import Product
from django import forms

all_products = Product.objects.all()


class CartForm(forms.Form):
    def __init__(self, *args):
        super(CartForm, self).__init__(*args)
        for product in Product.objects.all():
            product.name = forms.IntegerField()