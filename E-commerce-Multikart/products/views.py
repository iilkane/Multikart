from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from products.models import Product,Category,Brand,Size,Color
from core.models import ProductComment
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from core.forms import CommentForm
from django.urls import reverse_lazy
from accounts.models import Wishlist
from order.models import Cart 
from decimal import Decimal
from django.contrib import messages

# Create your views here.

class ProductListView(ListView):
    template_name = 'category-page.html'
    model = Product
    context_object_name = 'products'  # Product.objects.all()

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        search = self.request.GET.get('searched')
        sort = self.request.GET.get('sort')
        price = self.request.GET.get('price')
        if search:
            queryset = queryset.filter(title__icontains = search)
        if category:
            queryset = queryset.filter(category__id = category)
        if brand:
            queryset = queryset.filter(brand__id = brand)
        if color:
            queryset = queryset.filter(color__id = color)
        if size:
            queryset = queryset.filter(size__id = size)
        if category and brand:
            queryset = queryset.filter(category__id = category , brand__id = brand)
        if price:
            queryset = queryset.filter(price = price)


        if sort == 'price':
            queryset = queryset.order_by('price')
        elif sort == 'date':
            queryset = queryset.order_by('-created_at')
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['latest_products']=Product.objects.order_by("-created_at")[:4]
        context['brands']=Brand.objects.all()
        context['colors']=Color.objects.all()
        context['sizes']=Size.objects.all()
        return context


# def category(request):
#     products = Product.objects.all()
#     latest_products=Product.objects.order_by("-created_at")[:4]
#     brands=Brand.objects.all()
#     sizes=Size.objects.all()
#     context = {

#         "product_lists" : products,
#         "latest_products":latest_products,
#         "brands" : brands,
#         "sizes" :sizes
#     }

#     return render(request, 'category-page.html',context)


class ProductDetailView(FormMixin , DetailView):
    template_name = 'product-page.html'
    model = Product
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse_lazy('product_detail', kwargs = {'slug' : self.object.slug})

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     product_id = kwargs.get('pk')
    #     recently_viewed = request.session.get('recently_viewed', [])
    #     if product_id not in recently_viewed:
    #         recently_viewed.insert(0, product_id)
    #         request.session['recently_viewed'] = recently_viewed[:3]
    #     self.recently_products = Product.objects.filter(pk__in=recently_viewed)
    #     return response

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        slug = kwargs.get('slug')
        if slug:
            try:
                product = Product.objects.get(slug=slug)
                recently_viewed = request.session.get('recently_viewed', [])
                if product.pk not in recently_viewed:
                    recently_viewed.insert(0, product.pk)
                    request.session['recently_viewed'] = recently_viewed[:3]
            except Product.DoesNotExist:
                pass  # Handle the case where product with given slug does not exist
        return response

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        recently_viewed = self.request.session.get('recently_viewed', [])
        context['recently_products'] = Product.objects.filter(pk__in=recently_viewed)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(category=product.category).exclude(id=product.id)[:6]
        return context
    
    def post(self,  request, *args , **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.product = self.object       
        form.save()
        return super().form_valid(form)
    

def like (request , pk):
        user=request.user
        product=Product.objects.get(id=pk)

        if not Wishlist.objects.filter(user=user,product=product).exists():
           Wishlist.objects.create(user=user,product=product)
           messages.add_message(request, messages.SUCCESS, "The product has been added to your wishlist.")
        else:
            messages.add_message(request, messages.INFO, "The product is already on your wishlist.")
            return redirect(reverse_lazy('category'))
 
        return redirect(reverse_lazy("category"))


def remove_from_wishlist(request, pk):
    user = request.user
    wishlist_item = Wishlist.objects.filter(user=user, product_id=pk)

    for wishlist in wishlist_item:
        wishlist.delete()

    return redirect(reverse_lazy("wishlist"))


def cart(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=pk)
        quantity = int(request.POST.get('quantity', 1))  
        user = request.user

        cart = Cart.objects.filter(user=user, product=product).first()
            
        if not cart:
            Cart.objects.create(user=user, product=product, quantity=quantity)
            messages.add_message(request, messages.SUCCESS, "The product has been added to your basket.")
        else:
            messages.add_message(request, messages.INFO, "The product is already in your basket.")

        return redirect(reverse_lazy("cart_page"))
        
    else:
        product = get_object_or_404(Product, id=pk)
        user = request.user

        if product.quantity > 0:
            cart = Cart.objects.filter(user=user, product=product).first()
            if not cart:
                Cart.objects.create(user=user, product=product, quantity=1)
                messages.add_message(request, messages.SUCCESS, "The product has been added to your basket.")
            else:
                messages.add_message(request, messages.INFO, "The product is already in your basket.")
            
            return redirect(reverse_lazy("category"))
        else:
            messages.add_message(request, messages.ERROR, "No stock for this product.")
            return redirect(reverse_lazy("category"))
            



def remove_from_cart(request, pk):
    user = request.user
    product = get_object_or_404(Product, id=pk)

    cart = Cart.objects.filter(user=user, product=product).first()
    if cart:
        cart.delete()

    return redirect(reverse_lazy("cart_page"))



def add_to_cart(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)

    if product.quantity > 0:
        wishlist_item = Wishlist.objects.filter(user=user, product=product).first()

        if wishlist_item:
            if not Cart.objects.filter(user=user, product=product).exists():
                Cart.objects.create(user=user, product=product)
                messages.add_message(request, messages.SUCCESS, "The product has been added to your basket.")
            else:
                messages.add_message(request, messages.INFO, "The product is already in your basket.")
        return redirect(reverse_lazy('cart_page'))        
    else:
        messages.add_message(request, messages.ERROR, "No stock for this product.")
        return redirect(reverse_lazy('wishlist'))
        




# def product_detail(request, pk ):
#     product=get_object_or_404(Product , id=pk)
#     categories = Category.objects.all()
#     product.view_count += 1
#     product.save()
    
#     arr = request.session.get('recently_viewed', [])[ :4]
#     if pk in arr:
#         arr.remove(pk)
#         recently_viewed_products = Product.objects.filter(pk__in = arr)
#     else:
#         recently_viewed_products = Product.objects.filter(pk__in = arr)
#         arr.append(pk)
#         request.session['recently_viewed'] = arr 
#     context = {
#         "product" : product,
#         "categories" : categories,
#         'recently_viewed_products' : recently_viewed_products
#     }
#     return render(request, 'product-page.html' , context)


