from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    nome = "Helô"
    return render_template('index.html')


@app.route('/usuario')
def usuario():
    usuario = {'nome': 'Helô', 'email': 'heloisasevf@gmail.com'}
    return render_template('index.html', title='Página do Usuário', usuario=usuario, nome=None)


@app.route('/dados', defaults = {"nome": "usuário comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}!'


@app.route('/semestre/<int:x>')
def semestre(x):
    return f'Você está no semestre' + str(x)


@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return f'Você pagou: '+ str(valor)


@app.route('/somar', defaults={"n1": 0, "n2": 0})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return render_template('somar.html', n1=n1, n2=n2, resultado=resultado)


@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "Acesso bloqueado (cadeado fechado)"
    else:
        return "Acesso permitido (cadeado aberto)"


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


@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/')
@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')


@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/cliente/<nome>/lanche/<sabor>')
def cliente(nome, sabor):
    return render_template('pagdinamica.html', nome=nome, sabor=sabor)

if __name__ == '__main__':
    app.run(debug=True)
