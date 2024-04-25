from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from grocery_chains.filters import GroceryChainFilter
from grocery_chains.models import GroceryChain
from grocery_chains.serializers import GroceryChainSerializer


class GroceryChainViewSet(viewsets.ModelViewSet):
    queryset = GroceryChain.objects.all()
    serializer_class = GroceryChainSerializer
    filterset_class = GroceryChainFilter
    filter_backends = [DjangoFilterBackend]
