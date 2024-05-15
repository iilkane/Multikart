from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from accounts.models import ShippingAdress
from products.models import Product
# from products.models import ProductVersion


# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey( User , related_name='carts', on_delete=models.CASCADE)
    product = models.ForeignKey(Product ,related_name ='carts',on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title


class Checkout(models.Model):
     user=models.ForeignKey( User , related_name='checks', on_delete=models.CASCADE)
     adress=models.ForeignKey( ShippingAdress , related_name='checks', on_delete=models.CASCADE)
     cart=models.OneToOneField(Cart, related_name='checks', on_delete=models.CASCADE)
     transaction_code=models.CharField('transaction_code', max_length=100)


