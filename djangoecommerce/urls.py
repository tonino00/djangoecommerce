
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.contrib.auth.views import LoginView, LogoutView

from core import views
# from catalog import views as views_catalog

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^entrar/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^sair/$', LogoutView.as_view(next_page='index'), name='logout'),
    url(r'^catalogo/',  include(('catalog.urls', 'catalog'), namespace='catalog')),
    url(r'^conta/',  include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^admin/', admin.site.urls),
]
