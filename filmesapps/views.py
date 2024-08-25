from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano_lancamento']
        widgets = {
            'ano_lancamento': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
        }
