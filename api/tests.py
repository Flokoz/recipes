from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Chef, Recipes


class RecipesTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='Lucas', password='teste123')
        chef = Chef.objects.create(user=user)
        Recipes.objects.create(
            chef=chef,
            recipe_name='Pão com manteiga',
            recipe='Pegar o pão e passar manteiga',
            prepare_time='00:05'
        )

    def test_recipes_find(self):
        recipe = Recipes.objects.get(recipe_name='Pão com manteiga')
        self.assertEqual(recipe.chef.user.username, 'Lucas')

    def test_recipes_create(self):
        chef = Chef.objects.first()
        recipe = Recipes.objects.create(
            chef=chef,
            recipe_name='Ovo frito',
            recipe='Pegar o ovo e fritar',
            prepare_time='00:10'
        )
        self.assertEqual(recipe.recipe_name, 'Ovo frito')
        self.assertEqual(len(Recipes.objects.all()), 2)

    def test_recipes_update(self):
        Recipes.objects.update(
            recipe_name='Ovo cozido',
            recipe='Pegar o ovo e cozinhar'
        )
        recipe = Recipes.objects.first()
        self.assertEqual(recipe.recipe_name, 'Ovo cozido')

    def test_recipes_delete(self):
        Recipes.objects.first().delete()
        self.assertEqual(len(Recipes.objects.all()), 0)
