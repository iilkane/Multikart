from django.template import Library
register = Library()
from products.models import Category



@register.simple_tag
def get_categories(limit):
    categories = Category.objects.all()[:limit]
    return categories


