from django.db import models
from django.urls import reverse_lazy
# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField('created_at',auto_now_add=True)
    updated_at = models.DateTimeField('updated_at',auto_now=True)

    class Meta:
        abstract = True


class Subscriber(AbstractModel):
    email = models.EmailField('email', max_length = 100, unique = True)

    def __str__(self) -> str:
        return self.email     


class Brand(models.Model):
    title=models.CharField('title',max_length=100)

    def __str__(self) -> str:
        return self.title  


class Color(models.Model):
    title = models.CharField('title',max_length=100)
    code = models.CharField('kod',max_length=100)

    def __str__(self) -> str:
        return self.title
    

class Size(models.Model):
    title = models.CharField('title',max_length=100)
    

    def __str__(self) -> str:
        return self.title 


class Product(AbstractModel):
    category = models.ForeignKey('Category', related_name= 'product', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', related_name ='product', on_delete=models.CASCADE)

    title = models.CharField('title',max_length=100)
    color=models.ForeignKey('Color',related_name= 'product', on_delete=models.CASCADE)
    size=models.ForeignKey('Size',related_name= 'product', on_delete=models.CASCADE, null= True, blank= True)
    quantity = models.IntegerField(default=10)
    price = models.DecimalField('price',max_digits=10, decimal_places=2)
    small_description = models.CharField('small_description',max_length=200)
    description = models.CharField('description',max_length=500)
    cover_image= models.ImageField('cover_image',upload_to='product_images/')
    image= models.ImageField('image', upload_to='product_images/')
    slug = models.SlugField('slug',max_length=200,null=True,blank=True)
    view_count = models.IntegerField("view_count", default=0)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs = {'slug' : self.slug})
    
    class Meta:
        ordering =  ['-created_at']


class ProductImage(AbstractModel):
    product = models.ForeignKey('Product',related_name='images',on_delete=models.CASCADE)
    image = models.ImageField('image',upload_to='product_images/')

    def __str__(self) -> str:
        return self.product.title


class Category (AbstractModel):
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null= True, blank= True)
    title = models.CharField('title',max_length=100)
    

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} - {self.title}'
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'



# class ProductVersion(models.Model):
#     product=models.ForeignKey(Product,related_name= 'versions', on_delete=models.CASCADE)
#     color=models.ForeignKey(Color,related_name= 'versions', on_delete=models.CASCADE)
#     size=models.ForeignKey(Size,related_name= 'versions', on_delete=models.CASCADE, null= True, blank= True)
#     title = models.CharField('title',max_length=100)
#     quantity = models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return self.title
    

class BlockedIps(AbstractModel):
    ip_address = models.GenericIPAddressField()