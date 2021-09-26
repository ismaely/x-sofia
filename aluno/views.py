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


# Create your views here.


def adicionarNovaInscricao(request):
    form = DisciplinaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Dsciplina registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            return HttpResponseRedirect(reverse('home:home'))

    context = {'form':form}
    return render (request, 'aluno/adicionarInscricao.html', context)

