from django.shortcuts import render, get_object_or_404

from .models import Receita

def index(request):
    # Execute o comando python manage.py loaddata initial-data.json 
    # para carregar os dados iniciais do modelo.

    # Para gerar esses dados a partir do banco de dados, use o 
    # comando python manage.py dumpdata <nome do app[.nome do modelo]>:
    #     python manage.py dumpdata receitas.Receita

    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
        # order_by(-'date_receita') => Ordem decrescente de data.
        # filter(publicada=True)    => Retorna apenas as notícias publicadas.

    dados = { 'receitas': receitas }

    return render(request, 'index.html', dados)

def receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    return render(request, 'receita.html', {'receita' : receita})

def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    return render(request, 'buscar.html', {'receitas': lista_receitas})
