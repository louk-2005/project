from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'password'}))
    password_check=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'check password'}))
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('Username already exists')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('Email already exists')
        return email
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check')
        if password and password_check and password != password_check:
            raise ValidationError('Passwords do not match')



