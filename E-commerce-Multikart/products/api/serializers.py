from products.models import Category , Brand , Product, Color, Size ,Subscriber
from rest_framework import serializers


class SubscriberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title'
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'title'
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'title'
        )


class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source='category.title')
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'small_description',
            'description',
            'cover_image',
            'image',
            'slug',
            'view_count'

        )


class ProductCreateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'small_description',
            'description',
            'cover_image',
            'image',
            'slug',
            'view_count'

        )