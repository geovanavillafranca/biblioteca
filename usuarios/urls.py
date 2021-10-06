from django.urls import __path__
from django.urls.conf import path
from . import views


urlpatterns = [
    # o name é para poder identificar no html quando for chamar uma funcao
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),
    path('valida_login/', views.valida_login, name="valida_login"),
    path('sair/', views.sair, name = 'sair')

]

