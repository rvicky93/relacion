from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.lista_eventos, name ='lista_eventos'),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.evento_detalle, name='evento_detalle'),
    url(r'^evento/nuevo/$', views.evento_nuevo, name='evento_nuevo'),
    url(r'^evento/(?P<pk>[0-9]+)/edit/$', views.evento_editar, name='evento_editar'),
    url(r'^evento/(?P<pk>\d+)/remove/$', views.evento_eliminar, name='evento_eliminar'),
    url(r'^persona/$', views.lista_personas, name ='lista_personas'),
    url(r'^persona/nueva/$', views.persona_nueva, name='persona_nueva'),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.persona_detalle, name='persona_detalle'),
    url(r'^persona/(?P<pk>[0-9]+)/edit/$', views.persona_editar, name='persona_editar'),
    url(r'^persona/(?P<pk>\d+)/remove/$', views.persona_eliminar, name='persona_eliminar'),
    url(r'^tipoEvento/$', views.lista_tipo, name ='lista_tipo'),
    url(r'^tipoEvento/nuevo/$', views.tipo_nuevo, name='tipo_nuevo'),
    url(r'^tipoEvento/(?P<pk>[0-9]+)/$', views.tipo_detalle, name='tipo_detalle'),
    url(r'^tipoEvento/(?P<pk>[0-9]+)/edit/$', views.tipo_editar, name='tipo_editar'),
    url(r'^tipoEvento/(?P<pk>\d+)/remove/$', views.tipo_eliminar, name='tipo_eliminar'),
]
