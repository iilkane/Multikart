from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import AbstractModel




# Create your models here.

class Contact(models.Model):
    firstName = models.CharField('firstName',max_length=100)
    lastName = models.CharField('lastName',max_length=100,null=True,blank=True)
    number= models.CharField('number',max_length=30)
    email = models.EmailField('email',max_length=40)
    message = models.TextField('message',max_length=255)




class Blog(AbstractModel):
    user=models.ForeignKey( User , related_name='Blog', on_delete=models.CASCADE)
    title=models.CharField('title', max_length=100)
    description=models.TextField('description',max_length=200)
    cover_image= models.ImageField('cover_image',upload_to='blog_images/' ,null= True, blank= True)
    image= models.ImageField('image', upload_to='blog_images/' ,null= True, blank= True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    def get_image(self):
        if self.image:
            return self.image.url
        return 'static/image/depositphotos_318221368-stock-illustration-missing-picture-page-for-website.jpg'




