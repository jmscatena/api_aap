from django.urls import path
from treino import views


urlpatterns = [
    path('ex/add/', views.novo_exercicio),
    path('ex/', views.lista_exercicios, name="qexercicios"),
    path('ex/del/<int:num>', views.apaga_exercicio, name='dexercicio'),

]
