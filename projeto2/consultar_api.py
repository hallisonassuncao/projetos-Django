import requests

# Endereço da API Django
url = "http://127.0.0.1:8000/api/pessoas/"

try:
    # Faz a requisição GET para consultar as pessoas
    resposta = requests.get(url, timeout=10)

    # Verifica se a requisição foi bem-sucedida
    resposta.raise_for_status()

    # Converte o JSON recebido em dados Python
    dados = resposta.json()

    # Trata respostas paginadas do Django REST Framework
    if isinstance(dados, dict):
        pessoas = dados.get("results", [])
    else:
        pessoas = dados

    # Exibe os dados formatados
    print("\n" + "=" * 60)
    print("           SISTEMA DE CONSULTA DE PESSOAS")
    print("=" * 60)

    if pessoas:
        for pessoa in pessoas:
            print(f"ID:     {pessoa.get('id', 'N/A')}")
            print(f"Nome:   {pessoa.get('nome', 'N/A')}")
            print(f"Cidade: {pessoa.get('cidade', 'N/A')}")
            print("-" * 60)

        print(f"Total de pessoas: {len(pessoas)}")
    else:
        print("Nenhuma pessoa cadastrada.")

except requests.exceptions.RequestException as erro:
    print(f"Erro ao consultar a API: {erro}")