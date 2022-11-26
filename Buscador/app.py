from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__)

with open('bbdd.json', 'r') as openfile:
    json_object = json.load(openfile)

@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/index.html')

@app.route('/Busqueda', methods=['GET','POST'])
def Busqueda():
    if request.method == "POST":
        resultado = []
        search = ''
        search = request.form['buscar'].lower()
        # print('busqueda: ',search.split())
        if search != '':
            try:
                for busqueda in search.split():
                    resultadoaux = list(json_object[busqueda].keys())
                    for item in resultadoaux:
                        resultado.append(item)
            except:
                print()
            print('resultado: ', resultado)
            return render_template('public/resultado.html', resultado = resultado, busqueda = search)

@app.route('/Archivo/<archivo>', methods=['GET'])
def Archivo(archivo):
    if int(archivo) <= 5:
        file_path = "Carpeta1"
    else:
        file_path = "Carpeta2"

    file_input = requests.get("http://hadoop:5000/get/file/{}/Archivo{}".format(file_path, archivo)).content

    return render_template('public/archivo.html', resultado = file_input)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug = True, threaded = True)


