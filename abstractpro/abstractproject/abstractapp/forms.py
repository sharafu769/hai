# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class AdminRegistrationForm(UserCreationForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='admin')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class TeacherRegistrationForm(UserCreationForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='teacher')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class StudentRegistrationForm(UserCreationForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='student')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):

            pass

