from flask import Flask, render_template

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "Acesso bloqueado (cadeado fechado)"
    else:
        return "Acesso permitido (cadeado aberto)"
    

@app.route('/operacao/<tipo>/<float:n1>/<float:n2>')
def operacao(tipo, n1, n2):
    if tipo == 'soma':
        resultado = n1 + n2
    elif tipo == 'subtracao':
        resultado = n1 - n2
    elif tipo == 'divisao':
        resultado = n1 / n2 if n2 != 0 else "Divisão por zero não permitida"
    else:
        resultado = n1 * n2
        return resultado

    return render_template('operações.html', tipo=tipo, n1=n1, n2=n2, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
