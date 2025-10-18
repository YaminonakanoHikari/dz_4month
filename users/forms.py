from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField 
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'middle_name', 'email',
            'phone', 'birth_date', 'city', 'position', 'skills', 'experience',
            'github', 'linkedin', 'portfolio', 'password1', 'password2'
        ]

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()  
