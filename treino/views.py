from django.shortcuts import render, get_object_or_404, redirect
from treino.forms import ExerciciosForm,ExerciciosTreinoForm,TreinosForm
from treino.models import Exercicios,ExerciciosTreino,Treinos
from django.utils.html import format_html
# Create your views here.
def novo_exercicio(request):
  if request.method == 'POST':
    # Pegar os dados do Formulario do Cliente e vai validar no server
    form = ExerciciosForm(request.POST)
    if form.is_valid(): # se o formulario for valido...request
      form.save() # salva o formulario na tabela 
      command = format_html('<div class="alert alert-success"><h4>Cadastro Realizado com Sucesso!</h4></div>')    
      context = {'form': form, 'alert': command }
      return render(request, 'cadastros/exercicios.html', context)
  else:
    form = ExerciciosForm()  
  return render(request, 'cadastros/exercicios.html', {'form':form})

def lista_exercicios(request, id=0):
  exercicios = Exercicios.objects.all()
  if id !=0:
    if request.method == 'POST':
        form = ExerciciosForm(request.POST)
        if form.is_valid():
            exercicio = Exercicios.objects.get(descricao__icontains=form.cleaned_data.get('descricao'))
  else:
    exercicios = ExerciciosForm()
  return render(request, 'consultas/exercicios.html', {'exercicios':exercicios,'exercicio':exercicio})

def apaga_exercicio(request, id=0):
    exercicio = get_object_or_404(Exercicios, pk=id)
    form = ExerciciosForm(request.POST or None, instance=exercicio)
    if request.method == 'POST':
        form.delete()
    return redirect('qexercicios')

def altera_exercicio(request):
  if request.method == 'POST':
    # Pegar os dados do Formulario do Cliente e vai validar no server
    form = ExerciciosForm(request.POST)
    if form.is_valid(): # se o formulario for valido...request
      form.save() # salva o formulario na tabela 
      command = format_html('<div class="alert alert-success"><h4>Cadastro Realizado com Sucesso!</h4></div>')    
      context = {'form': form, 'alert': command }
      return render(request, 'cadastros/exercicios.html', context)
  else:
    form = ExerciciosForm()  
  return render(request, 'cadastros/exercicios.html', {'form':form})







def novo_treino(request):
  if request.method == 'POST':
    # Pegar os dados do Formulario do Cliente e vai validar no server
    form = TreinosForm(request.POST)
    if form.is_valid(): # se o formulario for valido...request
      form.save() # salva o formulario na tabela 
      command = format_html('<div class="alert alert-success"><h4>Cadastro Realizado com Sucesso!</h4></div>')    
      context = {'form': form, 'alert': command }
      return render(request, 'cadastros/treinos.html', context)
  else:
    form = TreinosForm()  
  return render(request, 'cadastros/treinos.html', {'form':form})

def novo_exerciciostreino(request):
  if request.method == 'POST':
    # Pegar os dados do Formulario do Cliente e vai validar no server
    form = ExerciciosTreinoForm(request.POST)
    if form.is_valid(): # se o formulario for valido...request
      form.save() # salva o formulario na tabela 
      command = format_html('<div class="alert alert-success"><h4>Cadastro Realizado com Sucesso!</h4></div>')    
      context = {'form': form, 'alert': command }
      return render(request, 'cadastros/exerciciostreino.html', context)
  else:
    form = ExerciciosTreinoForm()  
  return render(request, 'cadastros/exerciciostreino.html', {'form':form})