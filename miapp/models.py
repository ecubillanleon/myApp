#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Reportero(models.Model):
    nombre_completo = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.nombre_completo

class Articulo(models.Model):
    fecha_pub = models.DateTimeField(auto_now_add=True)
    encabezado = models.CharField(blank=False, max_length=200)
    contenido = models.TextField(blank=False,)
    reportero = models.ForeignKey(Reportero, blank=False)
    votos = models.IntegerField(default=0)

# Sí es python3 sería __str__
    def __unicode__(self): 
        return u'%s' % self.encabezado

    def fue_publicado_recientemente(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)
    fue_publicado_recientemente.admin_order_field = 'fecha_pub'
    fue_publicado_recientemente.boolean = True
    fue_publicado_recientemente.short_description = '¿Fue publicado recientemente?'
