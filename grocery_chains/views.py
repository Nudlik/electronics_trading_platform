from rest_framework import viewsets

from grocery_chains.models import GroceryChain
from grocery_chains.serializers import GroceryChainSerializer


class GroceryChainViewSet(viewsets.ModelViewSet):
    queryset = GroceryChain.objects.all()
    serializer_class = GroceryChainSerializer
