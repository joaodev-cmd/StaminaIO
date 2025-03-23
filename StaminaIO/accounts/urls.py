from django.urls import path
from . import views
from .views import custom_auth_token
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
    path('add/', views.createusu, name='add-user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
