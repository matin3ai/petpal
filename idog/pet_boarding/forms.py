from django import forms
from .models import Boarding

class BoardingForm(forms.ModelForm):
    class Meta:
        model = Boarding
        fields = ['name', 'address', 'contact_info', 'logo', 'conditions', 'costs', 'supported_animals', 'capacity', 'working_hours']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
            'conditions': forms.Textarea(attrs={'rows': 4}),
            'working_hours': forms.Textarea(attrs={'rows': 2}),
            'costs': forms.NumberInput(attrs={'step': '0.01'}),
        }