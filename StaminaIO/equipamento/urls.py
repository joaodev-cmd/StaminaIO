from django.urls import path
from . import views

urlpatterns = [
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
    path('equipamentos/adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('equipamentos/editar/<int:pk>/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/deletar/<int:pk>/', views.deletar_equipamento, name='deletar_equipamento'),
]
