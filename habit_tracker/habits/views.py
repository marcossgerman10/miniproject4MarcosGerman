from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('index')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'habits/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the home page
        else:
            return render(request, 'habits/login.html', {'error': 'Invalid username or password'})
    return render(request, 'habits/login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page


# Home page
@login_required
def index(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/index.html', {'habits': habits})

# Add habit
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('index')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})

# Edit habit
@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/edit_habit.html', {'form': form})

# Delete habit
@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    habit.delete()
    return redirect('index')

# Insights page
@login_required
def insights(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/insights.html', {'habits': habits})
