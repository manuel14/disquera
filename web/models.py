from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nac = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Disco(models.Model):
    nombre = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=None, null=True, blank=True)
    anio = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    imagen = models.ImageField(
        'Imagen', upload_to='images/', default='', blank=True, null=True)
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    descripcion = models.TextField()
