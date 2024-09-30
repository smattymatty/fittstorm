from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BaseApp.urls')),
    path('user/', include('UsersApp.urls')),
    path('dashboard/', include('dashboard_app.urls')),
    path('workouts/', include('workouts_app.urls')),
    path('nutrition/', include('nutrition_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
