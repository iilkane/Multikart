from django.urls import path
from products.views import ProductListView,ProductDetailView,like,cart,remove_from_cart,remove_from_wishlist,add_to_cart
urlpatterns = [
    path('category/', ProductListView.as_view() , name='category'),
    path('cart/<int:pk>/', cart , name='cart'),
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('like/<int:pk>/', like , name='like'),
    path('remove_from_wishlist/<int:pk>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('product/<str:slug>/', ProductDetailView.as_view() , name='product_detail'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    
]