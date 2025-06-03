import requests

def gerar_perfil_usuario():
    print("Gerador de Perfil de Usuário Aleatório")
    try:
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()
        dados = response.json()
        
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
    except KeyError:
        print("Erro: Não foi possível obter os dados do usuário. A estrutura da API pode ter mudado.")

gerar_perfil_usuario()
