from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipamentoViewSet

app_name = 'equipamento'
router = DefaultRouter()
router.register(r'equipamentos', EquipamentoViewSet)

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('editar/<int:pk>/', views.editar_equipamento, name='editar_equipamento'),
    path('deletar/<int:pk>/', views.deletar_equipamento, name='deletar_equipamento'),
    path('', include(router.urls)),
]
