from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from workouts_app.models import WorkoutSettings
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class WorkoutSettingsInline(admin.StackedInline):
    model = WorkoutSettings
    can_delete = False
    verbose_name_plural = 'workout settings'


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    def get_inline_instances(self, request, obj=None):
        inline_instances = super().get_inline_instances(request, obj)

        if obj:  # If the user exists
            try:
                # Check if the user has a WorkoutSettings instance
                if WorkoutSettings.objects.filter(user=obj).exists():
                    inline_instances.append(
                        WorkoutSettingsInline(self.model, self.admin_site))
            except WorkoutSettings.DoesNotExist:
                pass

        return inline_instances


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
