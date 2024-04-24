from django.contrib import admin, messages
from django.urls import reverse
from django.utils.safestring import mark_safe

from grocery_chains.models import GroceryChain
from products.models import Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(GroceryChain)
class GroceryChainAdmin(admin.ModelAdmin):
    list_display = ['name', 'debt', 'provider_link', 'country', 'city']
    list_filter = ['city']
    actions = ['clear_debts']
    inlines = [ProductInline]

    @admin.display(description='поставщик')
    def provider_link(self, obj):
        if not obj.provider:
            return 'Поставщик отсутствует'
        url = reverse('admin:grocery_chains_grocerychain_change', args=[obj.provider.pk])
        return mark_safe(f'<a href="{url}">{obj.provider}</a>')

    @admin.action(description='Обнулить долги поставщиков')
    def clear_debts(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, 'Долги обновлены', messages.SUCCESS)
