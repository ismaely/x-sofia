from django.db.models import Count, Exists, Q
from pessoa.models import Pessoa
from aluno.models import Aluno, Inscricao


def retorna_id(value):
    try:
        resp = Pessoa.objects.get(Q(bi=value) | Q(passaporte=value))
        if resp.id:
            return resp.id
    except Estudante.DoesNotExist:
        try:
            resp = Estudante.objects.get(numero_estudante=value)
            if resp.id:
                return resp.id
        except Estudante.DoesNotExist:
            return 0

