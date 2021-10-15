"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-09-26 13:00:26
 * @modify date 2021-09-26 13:00:26
 * @desc [description]
 */
"""
from django.shortcuts import render
from aluno.models import Aluno, Inscricao
from pessoa.forms import Pessoa_Form
from aluno.forms import Inscricao_Form
from django.http import HttpResponseRedirect
from django.urls import reverse
import json, sweetify



def adicionarNovaInscricao(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Inscricao_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save()
            dados = form.save(commit=False)
            dados.pessoa_id = pessoa.id
            sweetify.success(request, 'Dsciplina registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            context = {}
            return render (request, 'aluno/reciboInscricao.html', context)

    context = {'form':form,'form2':form2}
    return render (request, 'aluno/adicionarInscricao.html', context)

