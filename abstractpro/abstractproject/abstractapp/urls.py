# urls.py

from django.urls import path
from .views import  admin_register, teacher_register, student_register,login_view

urlpatterns = [

    path('login/', login_view, name='login'),
    path('admins/', admin_register, name='admin_register'),
    path('teacher/', teacher_register, name='teacher_register'),
    path('student/', student_register, name='student_register'),
    # Add other URLs as needed
]
