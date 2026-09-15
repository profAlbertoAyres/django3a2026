from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Aluno


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'E-mail'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'estado',
            'celular',
            'nascimento',
            'sexo',
            'objetivo',
        ]
        labels = {
            'nome': 'Nome',
            'cep': 'CEP',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'celular': 'Celular',
            'nascimento': 'Nascimento',
            'sexo': 'Sexo',
            'objetivo': 'Objetivo',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.TextInput(attrs={'class': 'form-control',
                                                 'type': 'date',}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
        }

