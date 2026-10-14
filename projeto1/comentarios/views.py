from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  # Renderizar templates e redirecionar
from .models import Comentario  # Modelo usado para persistência


# View para salvar um comentário e exibir o formulário e a lista
def salvar_comentario(request):
    # Se o método for POST, processa o envio do formulário
    if request.method == 'POST':
        autor = request.POST.get('autor')  # Obtém o nome do autor
        texto = request.POST.get('texto')  # Obtém o conteúdo do comentário

        # Cria uma instância do modelo
        comentario = Comentario(autor=autor, texto=texto)

        # Salva o comentário no banco de dados
        comentario.save()

        # Redireciona para evitar o reenvio do formulário
        return redirect('salvar_comentario')

    # Recupera os comentários do mais recente ao mais antigo
    comentarios = Comentario.objects.all().order_by('-data_criacao')

    # Renderiza o template com a lista de comentários
    return render(
        request,
        'comentarios/formulario.html',
        {'comentarios': comentarios}
    )

