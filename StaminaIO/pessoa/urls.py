# pessoa/urls.py

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, FuncionarioViewSet

app_name = 'pessoa'

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
urlpatterns = [

    #path('alunos/', views.listar_alunos, name='listar_alunos'),
    #path('alunos/adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    #path('alunos/editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    #path('alunos/deletar/<int:pk>/', views.deletar_aluno, name='deletar_aluno'),

    #path('alunos/pagar/<int:aluno_id>/', views.pagar_mensalidade, name='pagar_mensalidade'),
    #path('pagamento/<int:pagamento_id>/deletar/', views.deletar_pagamento, name='deletar_pagamento'),
    #path('alunos/<int:aluno_id>/pagamentos/', views.listar_pagamentos_aluno, name='listar_pagamentos_aluno'),
    #path('alunos/selecionar-pagamentos/', views.selecionar_aluno_pagamentos, name='selecionar_aluno_pagamentos'),

    #path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    #path('funcionarios/adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    #path('funcionarios/editar/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),
    #path('funcionarios/deletar/<int:pk>/', views.deletar_funcionario, name='deletar_funcionario'),

    path('', include(router.urls)), 
]
