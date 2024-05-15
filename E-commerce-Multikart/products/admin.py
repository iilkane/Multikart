from django.contrib import admin
from products.models import Category, Product, ProductImage,Color,Size,Brand,Subscriber,BlockedIps
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    fields = 'title',


admin.site.register(ProductImage)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Subscriber)
admin.site.register(BlockedIps)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','category']
    list_display_links = ['id','title',]
    list_editable = ['category']
    list_filter = ['category']
    search_fields = ['title']
    inlines = [ProductImageAdmin]
    # # prepopulated_fields = {
    # #     'slug' : ('title',)
    # }




   

