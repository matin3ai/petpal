from django import forms
from .models import LostPet
from pet_owner.models import Pet

class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        fields = ['pet', 'last_seen', 'date_lost', 'photo', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'last_seen': forms.Textarea(attrs={'rows': 2}),
            'date_lost': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)