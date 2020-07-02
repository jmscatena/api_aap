from django.shortcuts import render
from academia.models import Usuarios
from django.contrib.auth.models import User
from academia.forms import UsuariosForm
from django.utils.html import format_html
from django.db import transaction

@transaction.atomic
def novo_usuario(request):
  if request.method == 'POST':
    # Pegar os dados do Formulario do Cliente e vai validar no server
    form = UsuariosForm(request.POST)
    if form.is_valid(): # se o formulario for valido...request
      user = form.save() # salva o formulario na tabela
      user.refresh_from_db()
      userobj = User.objects.get(username=form.cleaned_data.get('username'))
      Usuarios.objects.create(user=userobj,
                    celular = form.cleaned_data.get('celular'),
                    urgtel = form.cleaned_data.get('urgtel'),
                    endereco = form.cleaned_data.get('endereco'),
                    numero = form.cleaned_data.get('numero'),
                    bairro = form.cleaned_data.get('bairro'),
                    cidade = form.cleaned_data.get('cidade'),
                    estado = form.cleaned_data.get('estado'),
                    professor = form.cleaned_data.get('professor'),
                    aluno = form.cleaned_data.get('aluno'),
                    gestor = form.cleaned_data.get('gestor'),)
      command = format_html('<div class="alert alert-success popup"><h4 style="text-align:center;">Cadastro de Cliente</h4><p style="text-align:center;">Realizado com Sucesso!</p></div>')
      context = {'form': form, 'alert': command }
      return render(request, 'cadastros/usuarios.html', context)
  else:
    form = UsuariosForm()  
  return render(request, 'cadastros/usuarios.html', {'form':form})

def lista_usuarios(request):
  usuarios = Usuarios.objects.all()#Select *
  return render(request, 'consultas/usuarios.html', {'usuarios':usuarios})

def lista_alunos(request):
  alunos = Usuarios.objects.filter(aluno__iexact=1)# Select Where aluno=True
  return render(request, 'consultas/alunos.html', {'alunos':alunos})

def lista_professores(request):
  professores = Usuarios.objects.filter(professor__iexact=1)
  return render(request, 'consultas/professores.html', {'professor':professores})

def lista_gestores(request):
  gestores = Usuarios.objects.filter(gestor__iexact=1)
  return render(request, 'consultas/gestores.html', {'gestores':gestores})