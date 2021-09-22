from django.shortcuts import render

# Create your views here.

def loginUser(request):
    context = {}
    return render (request, 'utilizador/login.html', context)

