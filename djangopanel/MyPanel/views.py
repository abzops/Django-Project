# filepath: c:\Users\Abhinand\OneDrive\Desktop\projects\django Project\djangopanel\MyPanel\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required
def index(request):
    sales = Project.objects.all()
    return render(request, 'Index.html', {'sales': sales})

def add_project(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        description = request.POST['description']
        deadline = request.POST['deadline']
        Project.objects.create(project_name=project_name, description=description, deadline=deadline)
        return redirect('index')
    return render(request, 'add_project.html')

def delete_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Signup successful! Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')