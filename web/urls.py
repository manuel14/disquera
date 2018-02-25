from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^discografia/', views.discografia, name='discografia'),
    url(r'^galeria/', views.galeria, name='galeria'),
    url(r'^prensa/', views.prensa, name='prensa'),
]
