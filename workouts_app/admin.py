from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise, WorkoutSettings


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'date', 'duration', 'estimated_calories']
    list_filter = ['user', 'date']
    search_fields = ['name', 'user__username']
    inlines = [WorkoutExerciseInline]


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'exercise_type',
                    'focus', 'estimated_calories_per_rep']
    list_filter = ['exercise_type', 'focus']
    search_fields = ['name', 'description']


@admin.register(WorkoutSettings)
class WorkoutSettingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'workouts_per_page']
    search_fields = ['user__username']


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ['workout', 'exercise', 'sets', 'reps',
                    'weight', 'distance', 'duration', 'rest_time']
    list_filter = ['workout', 'exercise']
    search_fields = ['workout__name', 'exercise__name']
