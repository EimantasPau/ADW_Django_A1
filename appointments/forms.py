from django import forms
from .models import Appointment

class NewAppointmentForm(forms.ModelForm):

    title = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Title'}), required=False)
    description = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Description'}), required=False)
    time = forms.CharField(label = '',widget=forms.TextInput(attrs={'id' : 'picker','size': 32, 'class': 'form-control', 'placeholder': 'Time'}), required=False)
    location = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Location'}), required=False)
    patient_name = forms.CharField(label = '',widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Patients name'}), required=False)
    # def clean(self, *args, **kwargs):
    #     title = self.cleaned_data['title']
    #     if not title:
    #         raise forms.ValidationError("The title field is required.")
    #     return super(NewAppointmentForm, self).clean(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title :
            raise forms.ValidationError("The title field is required.", )
        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        if not description:
            raise forms.ValidationError("The description field is required.", )
        return description

    def clean_time(self):
        time = self.cleaned_data['time']
        if not time:
            raise forms.ValidationError("The time field is required.", )
        return time

    def clean_location(self):
        location = self.cleaned_data['location']
        if not location:
            raise forms.ValidationError("The location field is required.", )
        return location

    def clean_patient_name(self):
        patient_name = self.cleaned_data['patient_name']
        if not patient_name:
            raise forms.ValidationError("The patient name field is required.", )
        return patient_name


    class Meta:
        model = Appointment
        fields = ('title', 'description', 'time', 'location', 'patient_name')





