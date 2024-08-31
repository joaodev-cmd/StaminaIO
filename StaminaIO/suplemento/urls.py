from django.urls import path
from . import views

app_name = 'suplemento'

urlpatterns = [
    path('', views.listar_suplementos, name='listar_suplementos'),
    path('adicionar/', views.adicionar_suplemento, name='adicionar_suplemento'),
    path('editar/<int:pk>/', views.editar_suplemento, name='editar_suplemento'),
    path('deletar/<int:pk>/', views.deletar_suplemento, name='deletar_suplemento'),
]
