from rest_framework import viewsets, filters

from .models import Pessoas
from .serializers import PessoasSerializer


class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

    # Permitir ordenação por nome, cidade e ID
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nome', 'cidade', 'id']
    ordering = ['id']

    # Permitir apenas GET e HEAD
    http_method_names = ['get', 'head']