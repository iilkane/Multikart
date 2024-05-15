from django.db import models
# from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import Product,AbstractModel


class ProductComment(AbstractModel):
    user = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE
    )
    message = models.TextField()
    rating=models.IntegerField(default=0,null=True,blank=True)
        
    def __str__(self) -> str:
        return f'{self.user.username} / {self.product}'