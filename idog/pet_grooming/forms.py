from django import forms
from .models import Grooming

class GroomingForm(forms.ModelForm):
    class Meta:
        model = Grooming
        fields = ['name', 'address', 'contact_info', 'photo', 'services', 'supported_animals', 'pricing', 'working_hours']
        widgets = {
            'services': forms.Textarea(attrs={'rows': 4}),
            'pricing': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 4}),
        }