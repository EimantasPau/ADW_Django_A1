from django.shortcuts import render
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
# Create your views here.


def login_view(request):
    if (request.method == "GET"):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if (request.method == "POST"):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               login(request,user)
               return redirect('/appointments')
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if (request.method == "GET"):
        form = RegistrationForm()
    if (request.method == "POST"):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username, email=email, password=password)
            user.save()
            auth_user = authenticate(username=username, password=password)
            print(auth_user)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('/appointments')
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/appointments')