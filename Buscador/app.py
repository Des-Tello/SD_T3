from flask import Flask, render_template, request, redirect, url_for, flash
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
        print('busqueda: ',search.split())
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
        file_input = open('Carpeta1/Archivo'+ archivo +'.txt', 'r').readline()
    else:
        file_input = open('Carpeta2/Archivo'+ archivo +'.txt', 'r').readline()

    return render_template('public/archivo.html', resultado = file_input)

if __name__ == "__main__":
    app.run(debug=True, port=8000)