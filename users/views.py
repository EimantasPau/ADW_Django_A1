from django.shortcuts import render
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
from django.shortcuts import redirect






from .forms import LoginForm
# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username');
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/appointments')
    return render(request, 'login.html', {'form':form})

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    return