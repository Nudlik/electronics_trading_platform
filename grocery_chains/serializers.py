from rest_framework import serializers

from grocery_chains.models import GroceryChain


class GroceryChainSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroceryChain
        exclude = ['owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        instance = self.Meta.model.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        validated_data['debt'] = instance.debt
        return super().update(instance, validated_data)
