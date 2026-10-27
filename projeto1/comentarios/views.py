
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Comentario


# View para salvar um comentário e exibir o formulário e a lista
def salvar_comentario(request):

    # Se o método for POST, processa o envio do formulário
    if request.method == 'POST':
        autor = request.POST.get('autor')
        texto = request.POST.get('texto')

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


# View para excluir um comentário
@require_POST
def excluir_comentario(request, id):

    # Busca o comentário pelo ID ou retorna erro 404
    comentario = get_object_or_404(Comentario, id=id)

    # Exclui o comentário do banco de dados
    comentario.delete()

    # Retorna à página principal
    return redirect('salvar_comentario')
