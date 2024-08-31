from django.urls import path
from . import views

app_name = 'equipamento'

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('editar/<int:pk>/', views.editar_equipamento, name='editar_equipamento'),
    path('deletar/<int:pk>/', views.deletar_equipamento, name='deletar_equipamento'),
]
