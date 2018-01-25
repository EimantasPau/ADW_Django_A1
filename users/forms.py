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