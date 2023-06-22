from django.db import models
from typing import Type, TypeVar
from django.db.models.query import QuerySet


# Create your models here.
"""class Cadastro(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.TextField(max_length=255)
    senha = models.IntegerField()
    objects = models.Manager()"""


class ComprasContrato(models.Model):
    id_time = models.BigIntegerField()
    id_processo = models.BigIntegerField()
    id_orgao_contrato = models.BigIntegerField()
    id_contrato = models.BigIntegerField()
    id_contratado = models.BigIntegerField()
    situacao_cont = models.BigIntegerField()
    ano_particao = models.BigIntegerField()
    vr_homologado = models.FloatField()
    vr_atualizado = models.FloatField()

    T = TypeVar('T', bound='ComprasContrato')
    objects: Type[T] = models.Manager()

    class Meta:
        db_table = 'ComprasContrato'

