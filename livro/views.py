from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros


# Create your views here.

def home(request):
    # verifica se tem um usuário logado
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        # pegando os livros cadastrados do usuario
        livros = Livros.objects.filter(usuario = usuario)
        


        return render(request, 'home.html', {'livros': livros})

    # se não estiver logado
    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    # pegando um unico livro, comparando os id's 
    livros = Livros.objects.get(id = id)

    return render(request, 'ver_livro.html', {'livro': livros})

