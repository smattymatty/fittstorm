from django import forms
from .models import Workout, Exercise, WorkoutExercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'duration', 'estimated_calories', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'ba-form-input'}),
            'duration': forms.TextInput(attrs={'class': 'ba-form-input'}),
            'estimated_calories': forms.NumberInput(attrs={'class': 'ba-form-input'}),
            'notes': forms.Textarea(attrs={'class': 'ba-form-input', 'rows': 3}),
        }


class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight',
                  'distance', 'duration', 'rest_time', 'notes']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'ba-form-input'}),
            'sets': forms.NumberInput(attrs={'class': 'ba-form-input'}),
            'reps': forms.NumberInput(attrs={'class': 'ba-form-input'}),
            'weight': forms.NumberInput(attrs={'class': 'ba-form-input', 'step': '0.1'}),
            'distance': forms.NumberInput(attrs={'class': 'ba-form-input', 'step': '0.1'}),
            'duration': forms.TextInput(attrs={'class': 'ba-form-input'}),
            'rest_time': forms.TextInput(attrs={'class': 'ba-form-input'}),
            'notes': forms.Textarea(attrs={'class': 'ba-form-input', 'rows': 2}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'exercise_type', 'focus',
                  'description', 'estimated_calories_per_rep']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'ba-form-input'}),
            'exercise_type': forms.Select(attrs={'class': 'ba-form-input'}),
            'focus': forms.Select(attrs={'class': 'ba-form-input'}),
            'description': forms.Textarea(attrs={'class': 'ba-form-input', 'rows': 3}),
            'estimated_calories_per_rep': forms.NumberInput(attrs={'class': 'ba-form-input'}),
        }
