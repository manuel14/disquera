from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^discografia/', views.discografia, name='discografia'),
    url(r'^galeria/', views.galeria, name='galeria'),
    url(r'^prensa/', views.prensa, name='prensa'),
    url(r'^quienes_somos/', views.quienes_somos, name='quienes_somos'),
    url(r'^eventos/', views.eventos, name='eventos'),
    url(r'^tinymce/', include('tinymce.urls')),
]
