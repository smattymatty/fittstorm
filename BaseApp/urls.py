from django.urls import path, include

from BaseApp import views

app_name = 'BaseApp'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
