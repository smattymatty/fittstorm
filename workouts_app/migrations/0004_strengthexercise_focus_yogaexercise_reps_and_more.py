# Generated by Django 5.1 on 2024-08-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts_app', '0003_alter_workout_duration_yogaexercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='strengthexercise',
            name='focus',
            field=models.CharField(choices=[('Full Body', 'Full Body'), ('Back', 'Back'), ('Chest', 'Chest'), ('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Legs', 'Legs'), ('Core', 'Core')], default='Body', max_length=100),
        ),
        migrations.AddField(
            model_name='yogaexercise',
            name='reps',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='yogaexercise',
            name='sets',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='yogaexercise',
            name='focus',
            field=models.CharField(choices=[('Flexibility', 'Flexibility'), ('Strength', 'Strength'), ('Balance', 'Balance'), ('Body', 'Body'), ('Mind', 'Mind'), ('Breath', 'Breath')], default='Body', max_length=100),
        ),
    ]