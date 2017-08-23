from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Reportero, Articulo
from .forms import ArticuloForm
from django.utils import timezone

# Create your views here.
def index(request):
    lista_ultimos_articulos = Articulo.objects.order_by('-votos')[:5]
    # Retornar vista sin template
    # salida = ', '.join([articulo.encabezado for articulo in lista_ultimos_articulos])
    # return HttpResponse(salida)

    # Retornar vista con template metodo largo
    # template  = loader.get_template('miapp/index.html')
    # context = RequestContext(request, {
    #	'lista_ultimos_articulos': lista_ultimos_articulos,
    # })
    #return HttpResponse(template.render(context))

    # Retornar vista con template metodo corto (Recomendado)
    context = {'lista_ultimos_articulos': lista_ultimos_articulos, 'numero': 20}
    return render(request, 'miapp/index.html', context)


def detalleArticulo(request, articulo_id):
    try:
	articulo = Articulo.objects.get(pk=articulo_id)
    except Articulo.DoesNotExist:
	raise Http404('El Articulo no existe!')
    return render(request, 'miapp/detallesArticulo.html', {
        'articulo': articulo,
        'sin_votar': True, 
    })


def resultados(request):
    return HttpResponse('Hola')


def votarPositivo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    articulo.votos += 1
    articulo.save()
    return render(request, 'miapp/detallesArticulo.html', {
        'articulo': articulo,
        'sin_votar': False, 
    })    

def votarNegativo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    articulo.votos -= 1
    articulo.save()
    return render(request, 'miapp/detallesArticulo.html', {
        'articulo': articulo,
        'sin_votar': False, 
    })


def new_articulo(request):
    if request.method == "POST":
	form = ArticuloForm(request.POST)
	if form.is_valid():
	   articulo = form.save()
	 # post.autor = request.user
	   articulo.save()
	   return render(request, 'miapp/detallesArticulo.html', {
               'articulo': articulo,
               'sin_votar': False,
          })

    else:
	form = ArticuloForm()
    return render(request, 'miapp/new_articulo.html', {'form':form})
