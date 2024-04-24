from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from grocery_chains.models import GroceryChain


@admin.register(GroceryChain)
class GroceryChainAdmin(admin.ModelAdmin):
    list_display = ['name', 'debt', 'provider_link', 'country', 'city']
    list_filter = ['city']

    @admin.display(description='поставщик')
    def provider_link(self, obj):
        if not obj.provider:
            return 'Поставщик отсутствует'
        url = reverse('admin:grocery_chains_grocerychain_change', args=[obj.provider.pk])
        return mark_safe(f'<a href="{url}">{obj.provider}</a>')
