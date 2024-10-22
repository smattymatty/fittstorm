# Generated by Django 5.1 on 2024-08-31 17:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts_app', '0004_strengthexercise_focus_yogaexercise_reps_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_ahead', models.IntegerField(default=5, help_text='Number of days ahead to view and schedule workouts')),
                ('days_behind', models.IntegerField(default=5, help_text='Number of days behind to view and schedule workouts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
