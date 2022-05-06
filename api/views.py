from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from api.models import Recipes
from api.serializers import RecipesSerializer


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

        View to filter recipes by name, chef's name or preparation time
        :param recipe_name: Will be received through query params and will be used to filter the recipe by name
        :type recipe_name: string
        :param chef_name: Will be received through query params and will be used to filter the recipe by chef's name
        :type chef_name: string
        :param prepare_time: Will be received through query params and will be used to filter the recipe by preparation time
        :type prepare_time: string
        :return: A list of recipes filtered by name, chef's name or preparation time

        """
        queryset = Recipes.objects.all().order_by('recipe_name')
        recipe_name = self.request.query_params.get('recipe_name')
        chef_name = self.request.query_params.get('chef_name')
        prepare_time = self.request.query_params.get('prepare_time')

        if recipe_name:
            queryset = queryset.filter(recipe_name=recipe_name)

        if chef_name:
            queryset = queryset.filter(chef__user__username=chef_name)

        if prepare_time:
            queryset = queryset.filter(prepare_time__lte=prepare_time)
        return queryset
