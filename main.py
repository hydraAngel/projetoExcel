from flask import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/clientes/abrir")
def cliAbrir():
    return render_template('clientes/abrir.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)