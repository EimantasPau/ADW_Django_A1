from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Appointment
# Create your views here.

def index(request):

    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'index.html', context)

def add(request):
    if(request.method == "GET"):
        return render(request,'create.html')

    if(request.method == "POST"):
        title = request.POST['title']
        description = request.POST['description']
        time = request.POST['time']
        location = request.POST['location']
        patient_name = request.POST['patient_name']
        appointment = Appointment(title=title, description=description, time=time, location=location, patient_name=patient_name)
        appointment.save()
        return redirect('/')
