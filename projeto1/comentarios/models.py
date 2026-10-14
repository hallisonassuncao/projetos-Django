from django.db import models

# Create your models here.
from django.db import models


# Modelo que representa um comentário simples
class Comentario(models.Model):
    autor = models.CharField(
        max_length=100
    )  # Nome do autor do comentário

    texto = models.TextField()  # Conteúdo do comentário

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )  # Data e hora de criação preenchidas automaticamente

    def __str__(self):
        # Retorna o autor e os primeiros 30 caracteres do comentário
        return f"{self.autor}: {self.texto[:30]}"