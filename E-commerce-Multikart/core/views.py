from django.shortcuts import render
from products.models import Product
from blog.models import Blog
from django.views.generic import ListView , DetailView
from django.db.models.query import QuerySet
from typing import Any
# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['latest_products']=Product.objects.order_by("-created_at")[:4]
        context['top_collection']=Product.objects.order_by("-created_at")[21:25]
        context['best_sellers']=Product.objects.order_by("-view_count")[:4]
        context['blogs'] = Blog.objects.all()
        return context

# def home(request):
#     product = Product.objects.all()
#     latest_product=Product.objects.order_by("-created_at")[:4]
#     latest_products=Product.objects.order_by("-created_at")[21:25]
#     context = {
#         "product" : product,
#         "latest_products":latest_products,
#         "latest_product" :latest_product
#     }
#     return render(request, 'index.html',context)


class SearchListView(ListView):
    template_name = 'search.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('searched')
        if search:
            queryset = queryset.filter(title__icontains = search)
        if category:
            queryset = queryset.filter(category__id = category)
        return queryset
    

# def search(request):
#     return render(request, 'search.html')

def notFound(request):
    return render(request,'404.html')

