from django.shortcuts import render
from academia.models import Usuarios
from django.contrib.auth.models import User
from academia.forms import UsuariosForm
from django.utils.html import format_html


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
      command = format_html('<div class="alert alert-success"><h4>Cadastro de Cliente</h4><p>Realizado com Sucesso!</p></div>')    
      context = {'form': form, 'alert': command }
      return render(request, 'clientes.html', context)

  else:
    form = UsuariosForm()  
  return render(request, 'clientes.html', {'form':form})
