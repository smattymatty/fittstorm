from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from .models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('UsersApp:profile')
    else:
        form = SignUpForm()
    return render(request, 'UsersApp/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('UsersApp:profile')
    else:
        form = LoginForm()
    return render(request, 'UsersApp/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'UsersApp/profile.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('UsersApp:login')


def home_view(request):
    if request.user.is_authenticated:
        return redirect('UsersApp:profile')
    else:
        return redirect('UsersApp:login')
