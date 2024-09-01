from django.urls import path

from equipamento.views import listar_equipamentos
from pessoa.views import listar_alunos, listar_funcionarios
from suplemento.views import listar_suplementos 
from .views import index

urlpatterns = [
    path('', index, name='index'), 
    path('alunos/', listar_alunos, name='lista_alunos'),
    path('funcionarios/', listar_funcionarios, name='lista_funcionarios'),
    path('equipamento/', listar_equipamentos, name='lista_equipamentos'),
    path('suplemento/', listar_suplementos, name='lista_suplementos'),
]

