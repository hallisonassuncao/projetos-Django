
import csv
from django.core.management.base import BaseCommand, CommandError
from livros.models import Autor, Livro


class Command(BaseCommand):
    help = 'Importa livros de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            'base_livros',
            type=str,
            help='Caminho do arquivo CSV'
        )

    def handle(self, *args, **kwargs):
        caminho = kwargs['base_livros']

        try:
            with open(
                caminho,
                newline='',
                encoding='utf-8-sig'
            ) as csvfile:

                reader = csv.DictReader(csvfile)

                colunas = {
                    'autor',
                    'titulo',
                    'isbn',
                    'paginas',
                    'ano_publicacao'
                }

                if not reader.fieldnames or not colunas.issubset(
                    reader.fieldnames
                ):
                    raise CommandError(
                        'O CSV deve conter as colunas: '
                        'autor, titulo, isbn, paginas, ano_publicacao'
                    )

                total = 0

                for numero, row in enumerate(reader, start=2):
                    try:
                        autor_nome = row['autor'].strip()

                        autor, _ = Autor.objects.get_or_create(
                            nome=autor_nome
                        )

                        Livro.objects.get_or_create(
                            titulo=row['titulo'].strip(),
                            autor=autor,
                            isbn=row['isbn'].strip(),
                            paginas=int(row['paginas']),
                            ano=int(row['ano_publicacao'])
                        )

                        total += 1

                    except (ValueError, TypeError) as erro:
                        raise CommandError(
                            f'Erro na linha {numero}: {erro}'
                        ) from erro

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Importação concluída! '
                        f'{total} registros processados.'
                    )
                )

        except FileNotFoundError as erro:
            raise CommandError(
                f'Arquivo CSV não encontrado: {caminho}'
            ) from erro
