from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('formulario.html')


@app.route('/autenticar', methods=['GET'])
def autenticar():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    return "{}, {} e {}".format(nome, curso, cidade)


if __name__ == '__main__':
    app.run(debug=True)
