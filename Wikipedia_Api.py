# import wikipedia

# wikipedia.set_lang("es")
# print(wikipedia.summary("Sexo"))
import requests
import json

entradas = ['Cristiano Ronaldo','Alexis Sanchez','Los Prisioneros','Alexis Sanchez','Dragon Ball','Colo-Colo','Diego Maradona','Messi','Santiago de Chile','Sabado gigante']

url = "https://en.wikipedia.org/w/api.php"
# params = {
#     'format': 'json',
#     'action': 'query',
#     'prop': 'extracts',
#     'exintro': '',
#     'explaintext': '',
#     'redirects': 1,
#     'titles': entradas[4]
# }
# req = requests.get(
#    url,
#    params=params
# ).json()

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
    texto = json.dumps(texto)
    if i <= 5:
        with open('./Carpeta1/Archivo'+str(i)+'.txt', 'w') as f:
            f.write(texto)
    else:
        with open('./Carpeta2/Archivo'+str(i)+'.txt', 'w') as f:
            f.write(texto)

    i = i + 1