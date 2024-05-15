from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from products.models import Product
from django.utils.text import slugify

@receiver(post_save, sender = Product)
def slug(instance, created,  *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + str(instance.id)
        instance.save()