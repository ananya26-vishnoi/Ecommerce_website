from django.contrib import admin

from .models import User, Admin, Product, Category, Cart, Buy
# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Buy)