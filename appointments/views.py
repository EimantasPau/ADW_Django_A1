from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
# Create your views here.

def index(request):

    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'index.html')