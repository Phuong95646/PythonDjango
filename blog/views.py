from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils.http import unquote
from django.contrib import messages
from django.template.response import TemplateResponse
from .models import Product
from .forms import CartForm
from django.shortcuts import redirect
from django.views.generic import View
from .models import Product, CartItem
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/home.html', {'products': products})

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     # Thêm logic để thêm sản phẩm vào giỏ hàng ở đây
#     return redirect('shopping_cart')

def buy_now(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Thêm logic để mua sản phẩm ở đây
    return redirect('order_confirmation')
def home(request):
    products = Product.objects.all()
    return render(request, 'blog/home.html', {'products': products})


def search(request):
    template = 'blog/home.html'
    query = request.GET.get('q')

    if query:
        # Giải mã query string
        query = unquote(query)

        # Tìm kiếm sản phẩm có tiêu đề, tên tác giả hoặc nội dung chứa query
        result = Product.objects.filter(name__icontains=query).order_by('name')
    else:
        result = Product.objects.all()

    # Số lượng sản phẩm trên mỗi trang
    page_size = 2

    # Phân trang kết quả
    paginator = Paginator(result, page_size)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'query': query}
    return render(request, template, context)

def getfile(request):
   return serve(request, 'File')


class PostListView(ListView):
    model = Product
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 2


class UserPostListView(ListView):
    model = Product
    template_name = 'blog/user_posts.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-created_at')


class PostDetailView(DetailView):
    model = Product
    template_name = 'blog/post_detail.html'
class AddToCartView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        # Thêm logic xử lý thêm vào giỏ hàng ở đây
        return redirect('home')

class BuyNowView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        # Thêm logic xử lý mua sản phẩm ở đây
        return redirect('home')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'blog/post_form.html'
    fields = ['name', 'quantity', 'price', 'image','title']
     


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'blog/home.html'



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'blog/post_form.html'
    fields = ['name', 'quantity', 'price', 'image','title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
from django.shortcuts import redirect, get_object_or_404
from .models import Product, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the customer is authenticated
    if request.session.get('Customer'):
        customer_id = request.session.get('Customer')
        
        # Check if the customer has an existing cart, create one if not
        user_cart, created = CartItem.objects.get_or_create(client_id=customer_id)

        # Check if the product is already in the cart, create a new item or update the quantity
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.quantity = 1
            cart_item.save()

        messages.success(request, 'Successfully added item to your cart!')

    return redirect('cart')


# def shopping_cart(request):
#     products = Product.objects.all()

#     if request.method == "POST":
#         form = CartForm(request.POST)
#         new_dict = dict(form.data)
#         new_dict.pop("csrfmiddlewaretoken")

#         if form.is_valid():
#             for product in new_dict:
#                 product_value = int(new_dict[product][0])
#                 product_instance = Product.objects.filter(name=product).first()

#                 if product_instance is None:
#                     messages.error(request, f"Product '{product}' not found.")
#                     return TemplateResponse(request, "template/cart.html", {"products": products})

#                 if product_instance.quantity == 0:
#                     messages.error(request, f"Sorry, We are out of {product_instance.name}")
#                     return TemplateResponse(request, "template/cart.html", {"products": products})

#                 if product_value > product_instance.quantity:
#                     messages.error(request, f"Sorry, We only have {product_instance.quantity}kg of {product_instance.name} left")
#                     return TemplateResponse(request, "template/cart.html", {"products": products})

#             # All products are valid and available
#             messages.success(request, "Your order has been validated successfully")
#             # Handle the rest of the logic for successful order submission here
#             return TemplateResponse(request, "template/cart.html", {"products": products})
#         else:
#             # Form is not valid
#             messages.error(request, "Invalid form data. Please correct the errors.")
#             return TemplateResponse(request, "template/cart.html", {"products": products})

#     return TemplateResponse(request, "template/cart.html", {"products": products})
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    # Lấy thông tin chi tiết của sản phẩm từ cơ sở dữ liệu
    product = get_object_or_404(Product, id=id)
    return render(request, 'blog/product_detail.html', {'product': product})
