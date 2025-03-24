from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import SuplementoViewSet

app_name = 'suplemento'

router = DefaultRouter()
router.register(r'', SuplementoViewSet)

urlpatterns = [
    #path('', views.listar_suplementos, name='listar_suplementos'),
    #path('adicionar/', views.adicionar_suplemento, name='adicionar_suplemento'),
    #path('editar/<int:pk>/', views.editar_suplemento, name='editar_suplemento'),
    #path('deletar/<int:pk>/', views.deletar_suplemento, name='deletar_suplemento'),
    path('', include(router.urls)),
]
