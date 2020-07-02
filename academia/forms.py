from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuariosForm(UserCreationForm):
  urgtel = forms.CharField(label='Telefone Emergencial', max_length=15, required=True)
  celular = forms.CharField(label='Celular', max_length=15, required=True)
  endereco = forms.CharField(label='Endereço',max_length=40, required=True)
  numero = forms.IntegerField(label='Número',required=True)
  bairro = forms.CharField(label='Bairro',max_length=20, required=True)
  cidade = forms.CharField(label='Cidade',max_length=25, required=True)
  estado = forms.CharField(label='Estado',max_length=2, required=True)
  professor = forms.BooleanField(required=False)
  aluno = forms.BooleanField(required=False)
  gestor = forms.BooleanField(required=False)

  class Meta:
    model = User
    fields = ('id','first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'endereco', 'numero','bairro', 'cidade', 'estado', 'urgtel', 'celular','professor', 'aluno', 'gestor')
  