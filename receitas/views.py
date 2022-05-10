from django.shortcuts import render, get_object_or_404

from .models import Receita

def index(request):
    receitas = Receita.objects.all()
    # Execute o comando python manage.py loaddata initial-data.json 
    # para carregar os dados iniciais do modelo.

    # Para gerar esses dados a partir do banco de dados, use o 
    # comando python manage.py dumpdata <nome do app[.nome do modelo]>:
    #     python manage.py dumpdata receitas.Receita

    dados = { 'receitas': receitas }

    return render(request, 'index.html', dados)

def receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    return render(request, 'receita.html', {'receita' : receita})
