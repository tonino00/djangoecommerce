
from django.conf.urls import url, include
from django.contrib import admin

from core import views
from catalog import views as views_catalog

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^catalogo/',  include(('catalog.urls', 'catalog'), namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]
