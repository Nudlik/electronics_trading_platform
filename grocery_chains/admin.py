from django.contrib import admin

from grocery_chains.models import GroceryChain


@admin.register(GroceryChain)
class GroceryChainAdmin(admin.ModelAdmin):
    pass
