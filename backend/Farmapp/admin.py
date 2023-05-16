from django.contrib import admin
from .models import Product
from .models import Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
