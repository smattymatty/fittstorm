from django.urls import path
from .views import WorkoutsPage

app_name = 'workouts'

urlpatterns = [
    path('', WorkoutsPage.as_view(), name='base'),
    path('<int:pk>/', WorkoutsPage.workout_detail, name='detail'),
    path('create/', WorkoutsPage.add_workout, name='add_workout'),
    path('user/', WorkoutsPage.workout_user_list, name='user_list'),
    path('excersises/add/',
         WorkoutsPage.add_exercise, name='add_exercise'),
    path('excercises/delete/<int:pk>/',
         WorkoutsPage.remove_exercise, name='remove_exercise'),
    path('exercises/user/', WorkoutsPage.exercise_user_list,
         name='exercise_user_list'),
    path('exercises/detail/<int:pk>/',
         WorkoutsPage.exercise_detail, name='exercise_detail'),
]
