from django.urls import path
from order.views import cart,checkout,order_success

urlpatterns = [
    path('cart_page/', cart , name='cart_page'),
    path('checkout/', checkout , name='checkout'),
    path('order_success/', order_success , name='order_success')
]