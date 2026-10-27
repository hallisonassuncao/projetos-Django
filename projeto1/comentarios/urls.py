
from django.urls import path
from .views import salvar_comentario, excluir_comentario

urlpatterns = [
    path('', salvar_comentario, name='salvar_comentario'),
    path(
        'excluir/<int:id>/',
        excluir_comentario,
        name='excluir_comentario'
    ),
]
