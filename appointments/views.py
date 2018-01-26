from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import NewAppointmentForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):

    if(request.GET.get('keyword')):
        keyword = request.GET.get('keyword')
        appointments = Appointment.objects.filter(
            Q(title__contains=keyword) | Q(description__contains=keyword) | Q(patient_name__contains=keyword)
        )
    else:
        appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'index.html', context)
@login_required
def add(request):
    if(request.method == "GET"):
        form = NewAppointmentForm()

    if(request.method == "POST"):
        form = NewAppointmentForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            time = form.cleaned_data.get('time')
            location = form.cleaned_data.get('location')
            patient_name = form.cleaned_data.get('patient_name')
            appointment = Appointment(title=title, description=description, time=time, location=location, patient_name=patient_name)
            appointment.save()
            messages.success(request, 'You have successfully created an appointment.')
            return redirect('/appointments')
    return render(request, 'create.html', {'form': form})
@login_required
def delete(request, pk):
    query = Appointment.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'Appointment deleted.')
    return redirect('/appointments')
@login_required
def edit(request, pk=None):

    if(request.method == "GET"):
        appointment = Appointment.objects.get(pk=pk)
        form = NewAppointmentForm(instance=appointment)
        return render(request, 'edit.html', {'form': form})

    if(request.method == "POST"):
        form = NewAppointmentForm(request.POST or None)
        appointment = Appointment.objects.get(pk=pk)
        if form.is_valid():
            appointment.title = form.cleaned_data.get('title')
            appointment.description = form.cleaned_data.get('description')
            appointment.time = form.cleaned_data.get('time')
            appointment.location = form.cleaned_data.get('location')
            appointment.patient_name = form.cleaned_data.get('patient_name')
            # appointment = Appointment(title=title, description=description, time=time, location=location,patient_name=patient_name)
            appointment.save()
            messages.success(request, 'You have successfully updated the appointment.')
            return redirect('/appointments')
        return render(request, 'create.html', {'form': form})