from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):

    produtos = Produto.objects.all()

    context = { 
        'curso': 'Programação web',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def produto(request, pk):
    #print(f'pk:{pk}')
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; chartset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


