from flask import Flask

app = Flask(__name__)

@app.route('/get/file/<name_file>')
def index(name_file):
    try:
        file = open('{}.txt'.format(name_file))
        return file.readlines()
    except:
        return "No Such File"