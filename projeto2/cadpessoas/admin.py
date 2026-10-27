from django.contrib import admin
from .models import Pessoas


@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade')
    search_fields = ('nome', 'cidade')