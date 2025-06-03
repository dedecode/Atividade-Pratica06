import requests
from datetime import datetime

def consultar_cotacao():
    print("Consulta de Cotação de Moeda")
    moeda_desejada = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_desejada}-BRL"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        if not dados:
            print("Moeda não encontrada ou dados indisponíveis.")
            return

        chave_moeda = f"{moeda_desejada}BRL"
        if chave_moeda not in dados:
            print(f"Não foi possível encontrar a cotação para {moeda_desejada}.")
            return
            
        cotacao = dados[chave_moeda]
        
        valor_atual = float(cotacao['bid'])
        valor_maximo = float(cotacao['high'])
        valor_minimo = float(cotacao['low'])
        timestamp_atualizacao = int(cotacao['timestamp'])
        
        data_hora = datetime.fromtimestamp(timestamp_atualizacao).strftime('%d/%m/%Y %H:%M:%S')
        
        print(f"Cotação de {moeda_desejada} para BRL:")
        print(f"Valor Atual: R${valor_atual:.4f}")
        print(f"Valor Máximo (24h): R${valor_maximo:.4f}")
        print(f"Valor Mínimo (24h): R${valor_minimo:.4f}")
        print(f"Última Atualização: {data_hora}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a cotação: {e}")
    except ValueError:
        print("Erro: Formato de dados inesperado da API.")
    except KeyError:
        print("Erro: Não foi possível obter os dados da cotação. A estrutura da API pode ter mudado.")

consultar_cotacao()
