from django.contrib import admin
from accounts.models import User ,ShippingAdress,Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product' ]

admin.site.register(User)
admin.site.register(ShippingAdress)
admin.site.register(Wishlist,WishlistAdmin)
