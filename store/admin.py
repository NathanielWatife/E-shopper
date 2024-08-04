from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(ProductReview)
admin.site.register(Order)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'shipping_address', 'profile_picture')
    search_fields = ('user__username', 'full_name')

admin.site.register(Profile, ProfileAdmin)