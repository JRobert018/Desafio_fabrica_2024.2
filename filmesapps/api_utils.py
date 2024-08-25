import requests

OMDB_API_KEY = ''  

def buscar_dados_filme(titulo):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={OMDB_API_KEY}"
    resposta = requests.get(url)
    return resposta.json()
