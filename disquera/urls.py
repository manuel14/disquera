"""disquera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from web import urls as web_urls
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'web.views.error404'
handler400 = 'web.views.error400'
handler500 = 'web.views.error500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(web_urls)),
    url(r'^_nested_admin/', include('nested_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
