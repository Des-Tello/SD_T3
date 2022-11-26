from flask import Flask

app = Flask(__name__)

@app.route('/get/file/<file_path>/<doc>')
def sex(file_path, doc):
    try:
        file = open('/home/hduser/examples/Wikipedia/{}/{}.txt'.format(file_path, doc))
        return file.readlines()[0]
    except:
        return "No Such File"

if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True, threaded = True)