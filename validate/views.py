"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-10-01 18:53:46
 * @modify date 2021-10-01 18:53:46
 * @desc [description]
 *
 """
from django.shortcuts import render
from django.db.models import Count, Exists, Q
from pessoa.models import Pessoa
from aluno.models import Aluno, Inscricao


def retorna_id(value):
    try:
        resp = Pessoa.objects.get(ndi=value)
        if resp.id:
            return resp.id
    except Pessoa.DoesNotExist:
        return 0

