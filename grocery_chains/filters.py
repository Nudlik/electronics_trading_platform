import django_filters

from grocery_chains.models import GroceryChain


class GroceryChainFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = GroceryChain
        fields = ['country']
