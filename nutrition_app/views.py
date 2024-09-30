from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .models import Ingredient, Meal
from .forms import IngredientForm, MealForm, MealIngredientFormSet

from BaseApp.utils import get_module_logger, check_htmx
from BaseApp.views import BasePage


class NutritionPage(BasePage):
    template_name = 'nutrition_app/base.html'
    page_title = "Nutrition"
    page_description = "This is the nutrition page."

    @login_required
    @staticmethod
    def add_ingredient(request):
        template = 'nutrition_app/add_ingredient.html'
        if request.method == 'POST':
            form = IngredientForm(request.POST)
            if form.is_valid():
                form.save()
                # You'll need to create this view
                return redirect('ingredient_list')
        else:
            form = IngredientForm()
        context = {'form': form}
        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))

    @login_required
    @staticmethod
    def add_meal(request):
        template = 'nutrition_app/add_meal.html'
        if request.method == 'POST':
            meal_form = MealForm(request.POST)
            ingredient_formset = MealIngredientFormSet(request.POST)
            if meal_form.is_valid() and ingredient_formset.is_valid():
                meal = meal_form.save(commit=False)
                meal.user = request.user
                meal.save()
                ingredient_formset.instance = meal
                ingredient_formset.save()
                # You'll need to create this view
                return redirect('nutrition:meal_list')
        else:
            meal_form = MealForm()
            ingredient_formset = MealIngredientFormSet()
        context = {
            'meal_form': meal_form,
            'ingredient_formset': ingredient_formset
        }
        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))

    @staticmethod
    def meal_detail(request, pk):
        template = 'nutrition_app/meal_detail.html'
        meal = get_object_or_404(Meal, pk=pk)
        context = {'meal': meal}

    @login_required
    @staticmethod
    def meal_user_list(request):
        template = 'nutrition_app/meal_user_list.html'
        meals = Meal.objects.filter(user=request.user)
        context = {'meals': meals}
        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))
