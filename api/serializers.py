from rest_framework import serializers

from api.models import Chef, Recipes


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['user']


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['chef', 'recipe_name', 'recipe', 'prepare_time']
