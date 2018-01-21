from django import forms
from .models import Appointment

class NewAppointmentForm(forms.ModelForm):

    title = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Description'}))
    time = forms.CharField(label = '',widget=forms.TextInput(attrs={'id' : 'picker','size': 32, 'class': 'form-control', 'placeholder': 'Time'}))
    location = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Location'}))
    patient_name = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Patients name'}))
    class Meta:
        model = Appointment
        fields = ('title', 'description', 'time', 'location', 'patient_name')


