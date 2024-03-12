# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm, TeacherRegistrationForm, StudentRegistrationForm
from .models import CustomUser, TeacherProfile, StudentProfile, AdminProfile
from django.contrib.auth.forms import AuthenticationForm

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            AdminProfile.objects.create(user=user, user_type='admin')
            return redirect('login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_register.html', {'form': form})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            TeacherProfile.objects.create(user=user, user_type='teacher')
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            StudentProfile.objects.create(user=user, user_type='student')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a specific page based on user type
            if user.is_superuser or user.admin_profile:
                return redirect('admin_dashboard')
            elif user.teacher_profile:
                return redirect('teacher_dashboard')
            elif user.student_profile:
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
