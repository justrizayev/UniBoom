from django.contrib import admin

# Register your models here.
from app_uniboom.models import Category, Product, User

admin.site.register(Category),
admin.site.register(Product),
admin.site.register(User)
