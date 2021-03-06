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
import json, sweetify, random, base64
from environment.env import DATA_HORA_ZONA 

"""
função que vai prepara a foto que vai ser salva
"""
def prepara_foto(request):
    img = request.POST["foto"]
    nome = str(DATA_HORA_ZONA).split('.')
    foto = []
    inicio = img.find(',')
    imagem = img[inicio+1:]

    with open("./media/fotos/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')

    um = um.replace("'", '')
    um = um.split('media/')
    return um[1]



def adicionarNovaInscricao(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Inscricao_Form(request.POST or None)
    if request.method == 'POST':
        form = Pessoa_Form(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            pessoa = form.save(commit=False)
            pessoa.municipio_id = form.cleaned_data.get('municipio')
            if len(request.POST['foto']) > 0:
                pessoa.foto = prepara_foto(request)
                pessoa.save()
            else:
                pessoa.foto ='user.jpg'
                pessoa.save()
            dados = form2.save(commit=False)
            dados.pessoa_id = pessoa.id
            dados.save()
            sweetify.success(request, 'Disciplina registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            context = {'pessoa': form.instance, 'inscricao': form2.instance}
            return render (request, 'aluno/reciboInscricao.html', context)

    context = {'form':form,'form2':form2}
    return render (request, 'aluno/adicionarInscricao.html', context)


def novaMaricula(request):
    pass


def listaInscricao(request):
    pass