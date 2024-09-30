from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.forms.models import inlineformset_factory

from .models import Workout, WorkoutSettings, WorkoutExercise, Exercise
from .forms import WorkoutForm, WorkoutExerciseForm, ExerciseForm

from BaseApp.views import BasePage
from BaseApp.utils import get_module_logger, check_htmx

module_logger = get_module_logger("views", __file__)


class WorkoutsPage(BasePage):
    template_name = 'workouts_app/base.html'
    page_title = "Workouts"
    page_description = "This is the workouts page."

    def get(self, request, *args, **kwargs):
        """
        Makes sure is authenticated and has a workout settings instance
        """
        if not request.user.is_authenticated:
            return redirect('UsersApp:login')
        else:
            user = request.user
            settings = WorkoutSettings.objects.get_or_create(user=user)[0]
            context = super().get_context_data(**kwargs)
            context['workouts_settings'] = settings

            return render(request, 'workouts_app/base.html', context)

    @staticmethod
    def workout_user_list(request):
        template = 'workouts_app/workout_user_list.html'
        if not request.user.is_authenticated:
            return redirect('UsersApp:login')
        workouts = Workout.objects.filter(user=request.user).order_by('-date')

        context = {'workouts': workouts}

        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))

    @login_required
    @staticmethod
    def workout_detail(request, pk):
        template = 'workouts_app/workout_detail.html'
        workout = get_object_or_404(Workout, pk=pk, user=request.user)
        context = {'workout': workout}
        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))

    @login_required
    @staticmethod
    def add_workout(request):
        template = 'workouts_app/add_workout.html'
        WorkoutExerciseFormSet = inlineformset_factory(
            Workout, WorkoutExercise, form=WorkoutExerciseForm, extra=1, can_delete=True
        )

        if request.method == 'POST':
            workout_form = WorkoutForm(request.POST)
            workout_exercise_formset = WorkoutExerciseFormSet(request.POST)

            if workout_form.is_valid() and workout_exercise_formset.is_valid():
                workout = workout_form.save(commit=False)
                workout.user = request.user
                workout.save()
                workout_exercise_formset.instance = workout
                workout_exercise_formset.save()

                if request.htmx:
                    return HttpResponse(
                        f'<div id="workout-create-form" hx-swap-oob="true">'
                        f'Workout "{workout.name}" created successfully!'
                        f'</div>'
                    )
                return redirect('workouts:detail', pk=workout.pk)
            else:
                module_logger.debug(
                    f"add_workout errors: {workout_form.errors} {workout_exercise_formset.errors}")
                # Pass form and formset errors to the context
                context = {
                    'workout_form': workout_form,
                    'workout_exercise_formset': workout_exercise_formset,
                }
                return HttpResponse(check_htmx(request, template, context))
        else:
            workout_form = WorkoutForm()
            workout_exercise_formset = WorkoutExerciseFormSet()

        context = {
            'workout_form': workout_form,
            'workout_exercise_formset': workout_exercise_formset,
        }

        return HttpResponse(check_htmx(request, template, context))

    @staticmethod
    @login_required
    def add_exercise(request):
        template = 'workouts_app/add_exercise.html'

        if request.method == 'POST':
            exercise_form = ExerciseForm(request.POST)

            if exercise_form.is_valid():
                exercise = exercise_form.save(commit=False)
                exercise.user = request.user
                exercise.save()
                if request.htmx:
                    # Return a fragment or a message suitable for HTMX
                    return HttpResponse(
                        f'<div id="exercise-create-form" hx-swap-oob="true">'
                        f'Exercise "{exercise.name}" created successfully!'
                        f'</div>'
                    )
                return redirect('workouts:exercise_detail', pk=exercise.pk)
            else:
                module_logger.debug(
                    f"add_exercise errors: {exercise_form.errors}")
                context = {'exercise_form': exercise_form}
                return HttpResponse(check_htmx(request, template, context))
        else:
            exercise_form = ExerciseForm()

        context = {'exercise_form': exercise_form}

        return HttpResponse(check_htmx(request, template, context))

    @staticmethod
    def remove_exercise(request, pk):
        print('lol')
        return HttpResponse('lol')

    @staticmethod
    def exercise_user_list(request):
        template = 'workouts_app/exercise_user_list.html'
        if not request.user.is_authenticated:
            return redirect('UsersApp:login')
        exercises = Exercise.objects.filter(
            user=request.user).order_by('-date')

        context = {'exercises': exercises}

        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))

    @staticmethod
    def exercise_detail(request, pk):
        template = 'workouts_app/exercise_detail.html'
        exercise = get_object_or_404(Exercise, pk=pk)
        context = {'exercise': exercise}
        return HttpResponse(check_htmx(
            request,
            template,
            context
        ))
