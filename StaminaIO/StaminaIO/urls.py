from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('index')),
    path('dashboard/', include('dashboard.urls')),
    path('pessoa/', include('pessoa.urls')),
    path('equipamento/', include('equipamento.urls')),
    path('suplemento/', include('suplemento.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('equipamento.urls')),
    path('api/pessoa/', include('pessoa.urls')),

]
