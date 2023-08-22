from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField, Value, F
from django.db.models.functions import Coalesce
from django.db.models import Count
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import ComprasContrato
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return render(request, 'usuarios/home_page.html')  # Redireciona para a página inicial após o login
        else:
            # Tratar caso de credenciais inválidas
            return render(request, 'usuarios/login.html', {'error_message': 'Credenciais inválidas'})
    else:
        return render(request, 'usuarios/login.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verifique se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            error_message = "Nome de usuário já existe. Escolha outro."
            return render(request, 'usuarios/cadastro.html', {'error_message': error_message})

        # Crie um novo usuário
        user = User(username=username, email=email, password=make_password(password))
        user.save()

        return render(request, 'usuarios/login.html')

    return render(request, 'usuarios/cadastro.html')


# @login_required
def home_page(request):
    return render(request, 'usuarios/home_page.html')


def consulta_ONE(request):
    resultados = ComprasContrato.objects.values('ano_particao').annotate(
        valor_homologado=Coalesce(Sum('vr_homologado', output_field=FloatField()), 0.0),
        valor_atualizado=Coalesce(Sum('vr_atualizado', output_field=FloatField()), 0.0)
    ).order_by('ano_particao')

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-1.html', {'resultados': resultados})


def consulta_TWO(request):
    resultados = ComprasContrato.objects.values('id_orgao_contrato').annotate(
        total_contratos=Count('*')
    ).order_by('-total_contratos')[:10]

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-2.html', {'resultados': resultados})


def consulta_TREE(request):
    resultados = ComprasContrato.objects.values('situacao_cont').annotate(
        valor_medio_atualizado=Avg('vr_atualizado')
    )

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-3.html', {'resultados': resultados})


def consulta_FOUR(request):
    resultados = ComprasContrato.objects.values('id_contratado').annotate(
        total_pagamentos=Sum('vr_atualizado')
    ).order_by('-total_pagamentos')[:10]

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-4.html', {'resultados': resultados})


def consulta_FIVE(request):
    resultados = ComprasContrato.objects.filter(vr_atualizado__gt=100000000)

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-5.html', {'resultados': resultados})


def consulta_SIX(request):
    resultados = ComprasContrato.objects.filter(vr_atualizado__lt=5000)

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-6.html', {'resultados': resultados})

def consulta_SEVEN(request):
    resultados = ComprasContrato.objects.order_by('-vr_homologado')[:10]

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-7.html', {'resultados': resultados})


def consulta_EIGTH(request):
    resultados = ComprasContrato.objects.annotate(diferenca_valores=F('vr_atualizado') - F('vr_homologado')).order_by('-diferenca_valores')[:10]

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-8.html', {'resultados': resultados})


def consulta_NINE(request):
    resultados = ComprasContrato.objects.values('id_orgao_contrato').annotate(
        aumento_valor=Sum('vr_atualizado') - Sum('vr_homologado')
    ).order_by('-aumento_valor')[:10]

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-9.html', {'resultados': resultados})


def consulta_TEN(request):
    resultados = ComprasContrato.objects.values('id_orgao_contrato').annotate(
        valor_total_homologado=Sum('vr_homologado'),
        valor_total_atualizado=Sum('vr_atualizado')
    ).order_by('id_orgao_contrato')

    # Renderize o template com os resultados
    return render(request, 'usuarios/consulta-10.html', {'resultados': resultados})


