from django.urls import path
from . import views

app_name = 'suplemento'

urlpatterns = [
    path('suplemento/', views.listar_suplementos, name='listar_suplementos'),
    path('suplemento/adicionar/', views.adicionar_suplemento, name='adicionar_suplemento'),
    path('suplemento/editar/<int:pk>/', views.editar_suplemento, name='editar_suplemento'),
    path('suplemento/deletar/<int:pk>/', views.deletar_suplemento, name='deletar_suplemento'),
]
