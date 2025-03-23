from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

def createusu(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UsuarioForm()
        return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login') 

@api_view(['POST'])
def custom_auth_token(request):
    view = ObtainAuthToken.as_view()
    response = view(request)
    token, created = Token.objects.get_or_create(user=response.data['user_id'])
    return Response({'token': token.key})
