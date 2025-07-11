from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'birth_date', 'species', 'breed', 'gender', 'color', 'appearance', 'photo', 'medical_history', 'qr_code_active']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'medical_history': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError("age must be a positive number.")
        if age > 30:  
            raise forms.ValidationError("age is too high, please check the birth date.")
        return age