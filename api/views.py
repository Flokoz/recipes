from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from api.models import Chef, Recipes
from api.serializers import ChefSerializer, RecipesSerializer


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all().order_by('user__username')
    serializer_class = ChefSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipesViewSet(viewsets.ModelViewSet):
    """
    View to list, add, remove and edit recipes
    """
    queryset = Recipes.objects.all().order_by('recipe_name')
    serializer_class = RecipesSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeSearch(ListAPIView):
    serializer_class = RecipesSerializer

    def get_queryset(self):
        """
        View to filter recipes by name and chef name
        :return: A list of recipes filtered by name or chef name
        """
        queryset = Recipes.objects.all().order_by('recipe_name')
        recipe_name = self.request.query_params.get('recipe_name')
        chef_name = self.request.query_params.get('chef_name')

        if recipe_name:
            queryset = queryset.filter(recipe_name=recipe_name)

        if chef_name:
            queryset = queryset.filter(chef__user__username=chef_name)

        return queryset
