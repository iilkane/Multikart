from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import AbstractModel,Product
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    number= models.CharField('number',max_length=50)
    message = models.CharField('message',max_length=100,null=True,blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null = True, blank = True)
    email = models.EmailField(("email address"), blank=True , unique=True)

    def get_total_cards_price(self):
        carts = self.carts.all()
        price = 0
        for element in carts:
            price += element.total_price()
        return price
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username',


class ShippingAdress(models.Model):
    user = models.ForeignKey(User,related_name='ShippingAdress', on_delete=models.CASCADE)
    flat = models.CharField('flat', max_length=100)
    address = models.TextField('address', max_length=300)
    zip_code = models.CharField('zip_code',max_length=10)
    country = models.CharField('country',max_length=100)
    city = models.CharField('city', max_length=100)
    region = models.CharField('region',max_length=100)


class Wishlist(models.Model):
    product = models.ForeignKey(Product ,related_name ='wishlist',on_delete = models.CASCADE)
    user = models.ForeignKey('User',related_name='wishlist', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'wishlists'

    def __str__(self):
        return self.product.title

    

