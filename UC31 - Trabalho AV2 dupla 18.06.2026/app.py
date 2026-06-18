from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votos = {
    "Netflix": 0,
    "Disney+": 0,
    "Prime Video": 0
}

@app.route('/')
def inicio():
    votou = request.cookies.get('votou')
    return render_template(
        'index.html',
        votou=votou,
        votos=votos
    )

@app.route('/votar/<opcao>')
def votar(opcao):

    if request.cookies.get('votou'):
        return redirect(url_for('resultado'))

    if opcao in votos:
        votos[opcao] += 1

        resp = redirect(url_for('resultado'))
        resp.set_cookie('votou', 'true')

        return resp

    return "Opção inválida", 404

@app.route('/resultado')
def resultado():

    total = sum(votos.values())

    porcentagens = {}

    for opcao, qtd in votos.items():
        if total > 0:
            porcentagens[opcao] = round((qtd / total) * 100, 2)
        else:
            porcentagens[opcao] = 0

    return render_template(
        'resultados.html',
        votos=votos,
        porcentagens=porcentagens,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True)