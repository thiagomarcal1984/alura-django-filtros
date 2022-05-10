from django.contrib import admin

from . import models

class ListandoReceitas(admin.ModelAdmin):
    # Opções disponíveis em https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options
    list_display = ('id', 'nome_receita', 'categoria')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',) # Busca num campo no topo.
    list_filter = ('categoria',) # Filtros em um painel à direita.
    list_per_page = 2 # Paginação após a tabela.

admin.site.register(models.Receita, ListandoReceitas)
