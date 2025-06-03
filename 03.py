import requests

def consultar_cep():
    print("Consulta de Endereço por CEP")
    cep = input("Digite o CEP (somente números): ")
    
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Digite 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        if 'erro' in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
            print(f"Bairro: {dados.get('bairro', 'Não informado')}")
            print(f"Cidade: {dados.get('localidade', 'Não informado')}")
            print(f"Estado: {dados.get('uf', 'Não informado')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")
    except KeyError:
        print("Erro: Não foi possível obter os dados do endereço. A estrutura da API pode ter mudado.")

consultar_cep()
