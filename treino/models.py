from django.db import models
#Importacao da classe usuario da app academia 
from academia.models import Usuarios

class Treinos(models.Model):
 id = models.BigAutoField(primary_key=True) 
 aluno = models.ForeignKey(Usuarios,related_name="taluno",on_delete=models.DO_NOTHING)
 professor = models.ForeignKey(Usuarios, related_name="tprofessor", on_delete=models.DO_NOTHING)
 descricao = models.CharField(max_length=20, blank=False)

class Exercicios(models.Model):
  id = models.BigAutoField(primary_key=True) 
  descricao = models.CharField(max_length=20, blank=False)
  
class ExercicioTreino(models.Model):
  id = models.BigAutoField(primary_key=True) 
  treino = models.ForeignKey(Treinos, blank=False, null=False, on_delete=models.CASCADE)
  exercicio = models.ForeignKey(Exercicios, blank=False, null=False, on_delete=models.DO_NOTHING)
  series = models.IntegerField(blank=False)
  repeticoes = models.IntegerField(blank=False)