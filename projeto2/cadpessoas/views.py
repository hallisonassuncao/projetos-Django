
from django.shortcuts import render
from rest_framework import viewsets

from .models import Pessoas
from .serializers import PessoasSerializer


# ViewSet para o recurso Pessoas.
# Fornece operações CRUD automaticamente:
# list, retrieve, create, update e destroy.
class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all().order_by('id')
    serializer_class = PessoasSerializer
