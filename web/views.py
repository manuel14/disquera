from django.shortcuts import render
from .models import Disco, Nota, Evento
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import os


def index(request):
    return render(request, 'web/index.html')


def discografia(request):
    letter = request.GET.get("letter", None)
    result = []
    if letter:
        discos = Disco.objects.filter(
            nombre__startswith=letter).order_by('artista__nombre')
    else:
        discos = Disco.objects.all().order_by('artista__nombre')

    for d in discos:
        dic = {}
        dic["pk"] = d.pk
        dic["nombre"] = d.nombre
        if d.artista:
            dic["artista"] = d.artista.nombre
        else:
            dic["artista"] = ""
        dic["imagen"] = d.imagen.url
        result.append(dic)

    json_clientes = json.dumps(result)
    return render(request, 'web/discografia.html',
                  {"discos": discos, "data": json_clientes})


def galeria(request):
    path = os.path.join(settings.MEDIA_ROOT, 'galeria')
    imagenes = []
    for file in os.listdir(path):
        if file.endswith(('.jpg', '.png', '.jpeg')):
            img = settings.URL_SERVER
            img += os.path.join(img, settings.MEDIA_ROOT, 'galeria', file)
            nombre = file.split(".")[0]
            dic = {"url": img, "nombre": nombre}
            imagenes.append(dic)
    print(imagenes)
    return render(request, 'web/galeria.html', {"imagenes": imagenes})


def prensa(request):
    notas = Nota.objects.all().order_by("-fecha")
    page = request.GET.get('page', 1)
    paginator = Paginator(notas, 5)
    try:
        page_notas = paginator.page(page)
    except PageNotAnInteger:
        page_notas = paginator.page(1)
    except EmptyPage:
        page_notas = paginator.page(paginator.num_pages)
    return render(request, 'web/prensa.html', {"notas": page_notas})


def eventos(request):
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'web/eventos.html', {"eventos": eventos})


def quienes_somos(request):
    return render(request, 'web/quienes_somos.html')
