from django import forms

from notas.models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('titulo', 'descripcion')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'})
        }
