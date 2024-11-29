from django.shortcuts import render
from .models import Produto

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
    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

    
