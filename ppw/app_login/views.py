from django.db.models import Sum, FloatField, Value, F
from django.db.models.functions import Coalesce
from django.db.models import Count
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import ComprasContrato


def listagem(request):
    # cc = ComprasContrato.objects.all()[:5000]
    cc = ComprasContrato.objects.all()
    return render(request, 'usuarios/listagem.html', {'cc': cc})


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
