from django.contrib import admin
import nested_admin
from .models import Disco, Artista, Nota, ImagenNota, VideoNota, Evento

admin.site.register(Disco)
admin.site.register(Artista)
admin.site.register(Evento)

class ImagenNotaInline(nested_admin.NestedStackedInline):
	model = ImagenNota
	extra = 1
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)

class VideoNotaInline(nested_admin.NestedStackedInline):
	model = VideoNota
	extra = 1
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)	

class NotaAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		VideoNotaInline,
		ImagenNotaInline,
	]
	exclude = ('text',)
	search_fields=('title__title',)
	

admin.site.register(Nota, NotaAdmin)