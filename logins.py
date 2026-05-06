from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/alunos')
def alunos():
    lista_alunos = [
        {'nome': 'Alice', 'matrícula': '12345678'},
        {'nome': 'Bruno', 'matrícula': '98765432'},
        {'nome': 'Clara', 'matrícula': '45678912'},
        {'nome': 'Marcos', 'matrícula': '74125896'},
        {'nome': 'Valéria', 'matrícula': '85236974'}
    ]

    return render_template('alunos.html', alunos=lista_alunos)


if __name__ == '__main__':
    app.run(debug=True)