from django import forms
from .models import Appointment, VetClinic
from pet_owner.models import Pet

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['vet_clinic', 'pet', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)
        self.fields['vet_clinic'].queryset = VetClinic.objects.all()

class VetClinicForm(forms.ModelForm):
    class Meta:
        model = VetClinic
        fields = ['name', 'address', 'contact_info', 'photo', 'services', 'supported_animals', 'license_number', 'working_hours']
        widgets = {
            'services': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 4}),
            'working_hours': forms.Textarea(attrs={'rows': 2}),
        }