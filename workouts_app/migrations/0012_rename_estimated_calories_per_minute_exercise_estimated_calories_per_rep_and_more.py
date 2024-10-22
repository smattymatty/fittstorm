# Generated by Django 5.1 on 2024-09-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts_app', '0011_rename_distance_exercise_default_distance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='estimated_calories_per_minute',
            new_name='estimated_calories_per_rep',
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='duration',
            field=models.DurationField(blank=True, default='00:00', null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='reps',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='rest_time',
            field=models.DurationField(blank=True, default='00:00', null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='sets',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True),
        ),
    ]
