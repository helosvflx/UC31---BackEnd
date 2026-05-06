from flask import Flask, render_template

app = Flask(__name__)

#questao1
@app.route('/ola/<nome>')
def saudacao(nome):
    return f"Olá, {nome}! Seja bem vindo ao sistema."


#questao2
@app.route('/somar', defaults={"n1": 0, "n2": 0})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return render_template(n1=n1, n2=n2, resultado=resultado)



#questao3
@app.route('/idade/<nome>/<int:idade>')
def idade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."

    return f"Olá, {nome}! Você tem {idade} anos."
#questao4
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f"O produto {nome} custa R${preco:.2f}."


#questao5
@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    resultado = (palavra + " ") * vezes
    return resultado.strip()

if __name__ == '__main__':
    app.run(debug=True)