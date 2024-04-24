from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'launch_date', 'creator']
    list_filter = ['launch_date', 'creator']
