from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.createusu, name='add-user'),
    path('success/', views.success_page, name='success_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
