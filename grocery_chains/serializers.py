from rest_framework import serializers

from grocery_chains.models import GroceryChain


class GroceryChainSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroceryChain
        fields = '__all__'
