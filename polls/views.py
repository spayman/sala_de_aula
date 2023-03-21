from django.http import HttpResponse


def index(request):
    return HttpResponse('Bem vindo!\n Você está na página index')
