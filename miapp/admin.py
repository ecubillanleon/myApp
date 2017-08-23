# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Reportero, Articulo

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['encabezado', 'fecha_pub', 'fue_publicado_recientemente']
    list_filter = ['fecha_pub']
    search_fields = ['encabezado']
    fieldsets = [
        (None, {'fields':['encabezado']}),
        (u'Información de Publicación', {'fields':['fecha_pub'], 'classes':['collapse']}),
        (u'Datos del Reportero', {'fields':['reportero']}),
    ]

admin.site.register(Reportero)
admin.site.register(Articulo, ArticuloAdmin)
