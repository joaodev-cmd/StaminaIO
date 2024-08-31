from django.urls import path
from . import views

app_name = 'pessoa'

urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('alunos/editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/deletar/<int:pk>/', views.deletar_aluno, name='deletar_aluno'),
    
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionarios/adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('funcionarios/editar/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/deletar/<int:pk>/', views.deletar_funcionario, name='deletar_funcionario'),
]
