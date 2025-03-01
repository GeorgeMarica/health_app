from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, VitalSignForm
from django.contrib.auth.decorators import login_required
from .models import VitalSign


# Home view (redirects to login)
def home(request):
    return render(request, 'health_app/home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'health_app/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'health_app/login.html', {'form': form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect('home')


# Dashboard (requires login)
@login_required
def dashboard(request):# Fetch the logged-in user's vital sign records
    vital_signs = VitalSign.objects.filter(user=request.user).order_by('-date')  # Show latest first
    return render(request, 'health_app/dashboard.html', {'vital_signs': vital_signs})


def record_vital_signs(request):
    if request.method == 'POST':
        form = VitalSignForm(request.POST)
        if form.is_valid():
            vital_sign = form.save(commit=False)
            vital_sign.user = request.user
            vital_sign.save()
            return redirect('dashboard')
    else:
        form = VitalSignForm()
    return render(request, 'health_app/record_vital_signs.html', {'form': form})
