# nutrition_app/forms.py
from django import forms
from .models import Ingredient, Meal, MealIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'calories_per_100g', 'other_nutrients']


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'estimated_calories',
                  'recipe', 'other_nutrients', 'meal_type']


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ['ingredient', 'amount', 'unit']


MealIngredientFormSet = forms.inlineformset_factory(
    Meal, MealIngredient, form=MealIngredientForm, extra=1, can_delete=True
)
