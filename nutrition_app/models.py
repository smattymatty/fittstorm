from django.db import models
from django.conf import settings


class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    estimated_calories = models.IntegerField(default=0)
    recipe = models.TextField(blank=True)
    other_nutrients = models.TextField(blank=True)
    meal_type = models.CharField(max_length=20, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ])

    def __str__(self):
        return f"{self.user.username}'s {self.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100g = models.IntegerField(default=0)
    other_nutrients = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MealIngredient(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='meal_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=20, choices=[
        ('g', 'Grams'),
        ('ml', 'Milliliters'),
        ('pcs', 'Pieces'),
        ('tbsp', 'Tablespoons'),
        ('tsp', 'Teaspoons'),
    ])

    def __str__(self):
        return f"{self.amount} {self.unit} of {self.ingredient.name} in {self.meal.name}"
