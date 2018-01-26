from django import forms
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)

User = get_user_model()

class LoginForm(forms.Form):
    username =  forms.CharField(label = 'Username',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'size': 32, 'class': 'form-control', 'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Incorrect username or password')
        return super(LoginForm, self).clean(*args, **kwargs)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Confirm password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError("User already exists.")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)

        if user:
            raise forms.ValidationError("Email already in use.")
        return email
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return super(RegistrationForm, self).clean()
