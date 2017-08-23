from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<articulo_id>[0-9]+)/$', views.detalleArticulo, name='detalleArticulo'),
    url(r'^(?P<articulo_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    url(r'^(?P<articulo_id>[0-9]+)/votarPositivo/$', views.votarPositivo, name='votarPositivo'),
    url(r'^(?P<articulo_id>[0-9]+)/votarNegativo/$', views.votarNegativo, name='votarNegativo'),
    url(r'^articulo/new/$', views.new_articulo, name='new_articulo'),
]
