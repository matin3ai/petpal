from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('owner', 'Pet owner'),
        ('vet', 'Vet'),
        ('boarding', 'Boarding'),
        ('grooming', 'Groomer'),
        ('store', 'Store'),
    ])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']