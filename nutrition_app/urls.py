from django.urls import path
from .views import NutritionPage

app_name = 'nutrition'

urlpatterns = [
    path('', NutritionPage.as_view(), name='base'),
    path('ingredients/add/', NutritionPage.add_ingredient, name='add_ingredient'),
    path('meals/add/', NutritionPage.add_meal, name='add_meal'),
    path('meals/user/', NutritionPage.meal_user_list, name='meal_list'),
    path('meals/<int:pk>/', NutritionPage.meal_detail, name='meal_detail'),
]
