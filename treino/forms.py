from django import ModelForm
from models import Exercicios,ExercicioTreino, Treinos
from academia.models import Usuarios


class TreinosForm(ModelForm):
  class Meta:
    model = Treinos
    field = '__all__' # pega todos os campos do meu ModelForm

class ExerciciosForm(ModelForm):
  class Meta:
    model = Exercicios
    field = '__all__' # pega todos os campos do meu ModelForm
  
class ExerciciosTreinoForm(ModelForm):
  class Meta:
    model = ExercicioTreino
    field = '__all__' # pega todos os campos do meu ModelForm
  