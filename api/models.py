from django.contrib.auth.models import User
from django.db import models


class Chef(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Recipes(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    recipe = models.CharField(max_length=500)
    prepare_time = models.TimeField()
