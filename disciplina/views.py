from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sweetify
from disciplina.forms import DisciplinaForm

# Create your views here.


def adicionarNovaDisciplina(request):
    form = DisciplinaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dsciplina registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            return HttpResponseRedirect(reverse('home:home'))

    context = {'form':form}
    return render (request, 'disciplina/adicionarDisciplina.html', context)

