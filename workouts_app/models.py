from django.db import models
from django.conf import settings

from .logic import determine_workout_type


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Workout")
    date = models.DateField(auto_now_add=True)
    duration = models.DurationField(
        help_text="Duration of workout", default="00:00")
    notes = models.TextField(blank=True)
    estimated_calories = models.IntegerField(
        help_text="Estimated calories burned (0 for unknown)", default=0)
    type = models.CharField(max_length=32, default="")

    def __str__(self):
        return f"{self.user.username}'s {self.name} on {self.date}"

    def get_workout_type(self):
        return determine_workout_type(self)

    def total_calories(self):
        return sum(exercise.calories for exercise in self.workoutexercise_set.all())

    def save(self, *args, **kwargs):
        if self.type is "":
            self.type = self.get_workout_type()
        return super().save(*args, **kwargs)


class Exercise(models.Model):
    EXERCISE_TYPES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('yoga', 'Yoga'),
    ]

    FOCUS_CHOICES = [
        ("Full Body", "Full Body"),
        ("Back", "Back"),
        ("Chest", "Chest"),
        ("Shoulders", "Shoulders"),
        ("Arms", "Arms"),
        ("Legs", "Legs"),
        ("Core", "Core"),
        ("Flexibility", "Flexibility"),
        ("Balance", "Balance"),
        ("Mind", "Mind"),
        ("Breath", "Breath"),
    ]

    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="exercises", default=0)
    date = models.DateField(auto_now_add=True)
    exercise_type = models.CharField(max_length=20, choices=EXERCISE_TYPES)
    focus = models.CharField(max_length=100, choices=FOCUS_CHOICES, blank=True)
    description = models.TextField(blank=True)
    estimated_calories_per_rep = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    # Fields for strength exercises
    default_weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    default_sets = models.IntegerField(null=True, blank=True)
    default_reps = models.IntegerField(null=True, blank=True)

    # Fields for cardio exercises
    default_distance = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    default_duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_exercise_type_display()})"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=0.0)
    distance = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=0.0)
    duration = models.DurationField(null=True, blank=True, default="00:00")
    rest_time = models.DurationField(null=True, blank=True, default="00:00")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"


class WorkoutSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workoutsettings")
    workouts_per_page = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.user.username}'s workout settings"
