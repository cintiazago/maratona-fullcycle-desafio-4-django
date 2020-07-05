from django.shortcuts import render
from .models import Aulas


def show_aulas(request):
    aulas = Aulas.objects.all()
    return render(request, 'aulas/index.html', {
        'aulas': aulas,
    })
