from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


usuario = ""
hash_senha = ""


@app.route("/", methods=["GET", "POST"])
def cadastro():
    global usuario, hash_senha

    if request.method == "POST":
        usuario = request.form["nome"]
        senha = request.form["senha"]

        # Gera o hash da senha
        hash_senha = generate_password_hash(senha)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    global usuario, hash_senha

    mensagem = ""

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]


        if nome != usuario:
            mensagem = "Usuário não encontrado."


        elif not check_password_hash(hash_senha, senha):
            mensagem = "Senha inválida."

        else:
            return redirect(url_for("inicio"))

    return render_template("login.html", mensagem=mensagem)


@app.route("/inicio")
def inicio():
    global usuario
    return render_template("inicio.html", usuario=usuario)


if __name__ == "__main__":
    app.run(debug=True)