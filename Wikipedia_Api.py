import requests
import json

entradas = ['Cristiano Ronaldo','Alexis Sanchez','Los Prisioneros','Alexis Sanchez','Dragon Ball','Colo-Colo','Diego Maradona','Messi','Santiago de Chile','Sabado gigante']
url = "https://en.wikipedia.org/w/api.php"
i = 1
for entrada in entradas:
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(
        url,
        params=params
    ).json()

    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']
    texto = json.dumps(texto) + "<end>"
    if i <= 5:
        with open('./Hadoop/Carpeta1/Archivo'+str(i)+'.txt', 'w') as f:
            f.write(texto)
    else:
        with open('./Hadoop/Carpeta2/Archivo'+str(i)+'.txt', 'w') as f:
            f.write(texto)
    i = i + 1