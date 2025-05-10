# filepath: c:\Users\Abhinand\OneDrive\Desktop\projects\django Project\djangopanel\MyPanel\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Project, Profile

# Ensure all users have a profile
for user in User.objects.all():
    Profile.objects.get_or_create(user=user)

@login_required(login_url='login')  # Restrict access to authenticated users
def index(request):
    sales = Project.objects.all()
    return render(request, 'Index.html', {'sales': sales})

@login_required(login_url='login')  # Restrict access to authenticated users
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        description = request.POST['description']
        deadline = request.POST['deadline']
        Project.objects.create(project_name=project_name, description=description, deadline=deadline)
        return redirect('index')
    return render(request, 'add_project.html')

@login_required(login_url='login')  # Restrict access to authenticated users
def delete_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect logged-in users to the index page
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
    if request.user.is_authenticated:
        return redirect('index')  # Redirect logged-in users to the index page
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

@login_required(login_url='login')  # Restrict access to authenticated users
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        user = request.user

        # Ensure the user has a profile
        profile, created = Profile.objects.get_or_create(user=user)

        # Update user fields
        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')

        # Update profile picture if provided
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        # Update password if provided
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))

        user.save()
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('index')
    return redirect('index')



def get_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return JsonResponse({
        "project_name": project.project_name,
        "description": project.description,
        "deadline": project.deadline.strftime('%Y-%m-%d'),
        "status": "active",  # Add a default status if it's not in the model
    })

def update_project(request, project_id):
    if request.method == "POST":
        project = get_object_or_404(Project, id=project_id)
        project.project_name = request.POST.get("project_name")
        project.description = request.POST.get("description")
        project.deadline = request.POST.get("deadline")
        project.save()  # Save the updated project to the database
        return JsonResponse({"success": True, "message": "Project updated successfully!"})
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=400)