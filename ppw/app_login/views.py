from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import ComprasContrato


"""def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        novo_usuario = Cadastro()
        novo_usuario.email = request.POST.get('email')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.save()

        usuarios = {
            'usuarios': Cadastro.objects.all()
        }
        return render(request, 'usuarios/listagem.html', {'usuarios': usuarios})


def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username,password=senha)

        if user:
            return HttpResponse('autenticado')
        else:
            return HttpResponse('e-mail ou senha incorretos')


def home(request):
    return render(request, 'usuarios/home.html')
    
cc = {
        'usuarios': ComprasContrato.objects.filter()
    }"""


def listagem(request):
    cc = ComprasContrato.objects.all()
    # print(cc)
    return render(request, 'usuarios/listagem.html', {'cc': cc})
