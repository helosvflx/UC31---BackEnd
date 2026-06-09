from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response
)

app = Flask(__name__)

@app.route('/')
def inicio():

    tema = request.cookies.get('tema', 'claro')
    nome = request.cookies.get('nome')

    return render_template(
        'inicio.html',
        tema=tema,
        nome=nome
    )


@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():

    nome = request.form.get('nome')

    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.set_cookie(
        'nome',
        nome,
        max_age=60*60*24*30
    )

    return resposta


@app.route('/tema/<escolha>')
def trocar_tema(escolha):

    if escolha not in ['claro', 'escuro']:
        escolha = 'claro'

    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.set_cookie(
        'tema',
        escolha,
        max_age=60*60*24*30
    )

    return resposta


@app.route('/limpar')
def limpar():

    resposta = make_response(
        redirect(url_for('inicio'))
    )

    resposta.delete_cookie('nome')
    resposta.delete_cookie('tema')

    return resposta


if __name__ == '__main__':
    app.run(debug=True)