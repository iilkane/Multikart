from products.models import Category,Brand ,Product,Color,Size ,Subscriber
from django.http import JsonResponse
from products.api.serializers import CategorySerializer, CategoryCreateSerializer,BrandSerializer,ProductSerializer,ProductCreateSerializer,ColorSerializer,SizeSerializer,SubscriberCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView , CreateAPIView ,ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly


class SubscriberCreateAPIView(CreateAPIView):
    serializer_class = SubscriberCreateSerializer
    queryset = Subscriber.objects.all()


class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CategoryCreateSerializer
        return self.serializer_class
    

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()
   

def categories(request):
    category_list = Category.objects.all()
    # category_dict = []
    # for category in category_list:
    #     category_dict.append({
    #         'category_id' : category.id,
    #         'category_title' : category.title

    #     })
    serializer = CategorySerializer(category_list, many=True)
    return JsonResponse(serializer.data , safe=False)


class ColorAPIView(ListAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class SizeAPIView(ListAPIView):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()


class BrandAPIView(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


def brand(request):
    brand_list = Brand.objects.all()
    serializer = BrandSerializer(brand_list, many = True)
    return JsonResponse(serializer.data , safe = False)


class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return self.serializer_class


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


def products(request):
    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list , many = True)
    return JsonResponse(serializer.data, safe = False)


@api_view(http_method_names=["GET" , "POST"])
def products(request):
    if request.method =='POST':
        serializer = ProductCreateSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data , safe = False , status = 201)
        return JsonResponse(serializer.errors , safe = False , status = 400)
    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list, context = {'request' : request }, many = True)
    return JsonResponse(serializer.data , safe= False)


@api_view(http_method_names=["PUT" , "PATCH"])
def product_update(request , pk):
    if request.method =='PUT':
        product = Product.objects.get(id = pk)
        serializer = ProductCreateSerializer(data = request.data , instance= product)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data , safe = False , status = 201)
        return JsonResponse(serializer.errors , safe = False , status = 400)
    if request.method =='PATCH':
        product = Product.objects.get(id = pk)
        serializer = ProductCreateSerializer(data = request.data , partial = True ,instance= product)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data , safe = False , status = 201)
        return JsonResponse(serializer.errors , safe = False , status = 400)
    return JsonResponse(serializer.data , safe= False)