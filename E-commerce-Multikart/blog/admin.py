from django.contrib import admin
from blog.models import Contact, Blog

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstName']
    # prepopulated_fields = {
    #     'fullName' : ('firstName','lastName')
    # }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title']
    actions = ['blog_activated','blog_deactivated']

    def blog_activated(self, request, queryset):
        queryset.update(ststus = True)

    def blog_deactivated(self, request, queryset):
        queryset.update(ststus = False)