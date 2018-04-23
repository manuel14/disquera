from django.shortcuts import render
from .models import Disco, Nota, Evento
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os


def index(request):
    return render(request, 'web/index.html')


def discografia(request):
    letter = request.GET.get("letter", None)
    if letter:
        discos = Disco.objects.filter(
            nombre__startswith=letter).order_by('artista__nombre')
    else:
        discos = Disco.objects.all().order_by('artista__nombre')
    return render(request, 'web/discografia.html',
                  {"discos": discos})


def galeria(request):
    path = os.path.join(settings.MEDIA_ROOT, 'galeria')
    imagenes = []
    for file in os.listdir(path):
        if file.endswith(('.jpg', '.png', '.jpeg')):
            img = settings.URL_SERVER
            img += os.path.join(img, settings.MEDIA_URL, 'galeria', file)
            # Para codificar caracteres que salen de utf8
            nombre = file.split(".")[0].encode('utf8', 'surrogateescape')
            dic = {"url": img, "nombre": nombre}
            imagenes.append(dic)
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
    return render(request, 'web/lista_notas.html', {"notas": page_notas})


def nota(request):
    pk = request.GET.get("pk", None)
    n = Nota.objects.get(pk=int(pk))
    return render(request, 'web/prensa.html', {"nota": n})


def eventos(request):
    eventos = Evento.objects.all().order_by('-fecha')
    page = request.GET.get('page', 1)
    paginator = Paginator(eventos, 5)
    try:
        page_eventos = paginator.page(page)
    except PageNotAnInteger:
        page_eventos = paginator.page(1)
    except EmptyPage:
        page_eventos = paginator.page(paginator.num_pages)
    return render(request, 'web/lista_eventos.html', {"eventos": page_eventos})


def evento(request):
    evento = request.GET.get("nombre", None)
    e = Evento.objects.get(nombre=evento)
    return render(request, 'web/evento.html', {"evento": e})


def quienes_somos(request):
    return render(request, 'web/quienes_somos.html')


def nosotros(request):
    return render(request, 'web/nosotros.html')


def error400(request):
    return render(request, 'web/400.html')


def error404(request):
    return render(request, 'web/404.html')


def error500(request):
    return render(request, 'web/500.html')
