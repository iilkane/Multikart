from django.urls import path
from products.api.views import CategoryAPIView, CategoryRetrieveUpdateDestroyAPIView,BrandAPIView,ProductListAPIView,ProductRetrieveUpdateDestroyAPIView,ColorAPIView,SizeAPIView,SubscriberCreateAPIView


urlpatterns = [
    path('subscriber/' , SubscriberCreateAPIView.as_view() , name='subscriber'),
    path('categories/' , CategoryAPIView.as_view() , name='categories'),
    path('category/<int:pk>/' , CategoryRetrieveUpdateDestroyAPIView.as_view() , name='category_update'),
    path('brand/' , BrandAPIView.as_view() , name='brand'),
    path('color/' , ColorAPIView.as_view() , name='color'),
    path('size/' , SizeAPIView.as_view() , name='size'),
    path('products/' , ProductListAPIView.as_view(), name='products'),
    path('product/<int:pk>/' , ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_update')
]