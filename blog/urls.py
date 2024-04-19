from django.urls import path
from .views import HomePageView, AddToCartView, BuyNowView, product_detail
from blog.views import product_list, add_to_cart, buy_now

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='blog-about'),
    path('products/', product_list, name='product-list'),
    path('add-to-cart/<uuid:product_id>/', add_to_cart, name='add-to-cart'),
    path('buy-now/<uuid:product_id>/', buy_now, name='buy-now'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    # path('shopping-cart/', views.shopping_cart, name='shopping_cart'),  
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add-to-cart'),
    # path('shopping-cart/',views.shopping_cart,name='shopping.cart'),
    # path('shopping-cart/process',views.process_order,name='shopping.process'),
    # path('cart/', views.cart_view, name='cart'),
    path('product/<uuid:id>/', product_detail, name='product-detail'),


]
