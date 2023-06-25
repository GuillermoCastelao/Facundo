from django import forms
from .models import Alumnos

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields='__all__'
        widgets = {
            'nacfecha': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }