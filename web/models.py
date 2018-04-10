from django.db import models
from tinymce import models as tinymce_models

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nac = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Disco(models.Model):
    nombre = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=None, null=True, blank=True)
    anio_pub = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(
        'Imagen', upload_to='images/', default='')
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    descripcion = tinymce_models.HTMLField()
    def htmlText(self, txt):
        texto = u'<p class="text-justify">'
        texto += txt.replace(u'\n', u'</p><p class="text-justify">')
        texto += u'\r</p>'
        texto = texto.replace(u'<p class="text-justify">\r</p>', u'')
        return texto

    def __str__(self):
        return self.titulo

class VideoNota(models.Model):
    nota = models.ForeignKey(
        Nota, on_delete=models.CASCADE, related_name="videos")
    link = models.FileField('Video', upload_to='videos/',
                            default='')

class ImagenNota(models.Model):
    nota = models.ForeignKey(
        Nota, on_delete=models.CASCADE, related_name="imagenes")
    link = models.ImageField("notaimage" ,upload_to='images/' )
    nombre = models.CharField(max_length=200)

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    foto = models.ImageField('foto', upload_to='images/')
    video = models.FileField(upload_to='videos/', blank=True, null=True)
