from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from api.views import RecipesViewSet, RecipeSearch

router = routers.DefaultRouter()

router.register(r'recipes', RecipesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipes-find/', RecipeSearch.as_view(), name='recipe_search'),
]
