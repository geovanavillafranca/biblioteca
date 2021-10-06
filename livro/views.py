from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # verifica se tem um usuário logado
    if request.session.get('usuario'):
        return HttpResponse('olá')
    # se não estiver logado
    else:
        return redirect('/auth/login/?status=2')
