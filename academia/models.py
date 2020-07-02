from django.db import models
from django.contrib.auth.models import User


#Estrutura basica para a criacao de uma tabela
class Usuarios(models.Model):
  id = models.BigAutoField(primary_key=True) # chave primaria
  # campo user tem os campos nome, sobrenome, email, username, pass
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  convmedico = models.CharField(max_length=15)
  urgtel = models.CharField(max_length=15, blank=False,default='')
  celular = models.CharField(max_length=15, blank=False)
  endereco = models.CharField(max_length=40, blank=False)
  numero = models.IntegerField(blank=False)
  bairro = models.CharField(max_length=20, blank=False)
  cidade = models.CharField(max_length=25, blank=False)
  estado = models.CharField(max_length=2, blank=False)
  professor = models.BooleanField(default=False)
  aluno = models.BooleanField(default=False)
  gestor = models.BooleanField(default=False)
  


  
  





