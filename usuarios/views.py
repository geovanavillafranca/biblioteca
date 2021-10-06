from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


# Create your views here.

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    # vai pegar a requisicao que foi utilizada com o POST
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    # verificando a duplicidade de um email de usuario dentro do banco de dados
    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    # verifica o tamanho, caso seja maior quer dizer que tem mais de um email,
    # não pode cadastrar
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        # o .encode torna em binario
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, senha = senha, email = email)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')

    except:
        return redirect('/auth/cadastro/?status=4')

    return HttpResponse(f"{nome} {email} {senha}")


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    # usuario nao existe
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    
    # usuario existe
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home')

    return HttpResponse(f"{email} {senha}")


# quando usuario sair
def sair(request):
    # limpando a session
    request.session.flush()
    return redirect('/auth/login/')

