
def determine_workout_type(workout):
    """
    Determines the type of workout based on the exercises in the workout.
    Returns a string representing the workout type.

    If there are more of one type of exercise, returns '{exercise_type}'.
    If there are the same number of two excersises, returns '{type1}/{type2}'.
    If there are an equal amount of each type (give or take total/10), returns 'All'.
    Otherwise, returns 'Other'.
    """
    from .models import Exercise
    return "lol"
    exercises = Exercise.objects.filter(
        id__in=workout.workoutexercise_set.all())
    strength_exercises = exercises.filter(exercise_type='strength')
    cardio_exercises = exercises.filter(exercise_type='cardio')
    yoga_exercises = exercises.filter(exercise_type='yoga')
