from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "napi2026"

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), "data", "banco.json")


# ----------------------------
# Funções auxiliares para o JSON
# ----------------------------

def carregar_dados():
    """Lê o banco.json. Se não existir, cria a estrutura inicial."""
    if not os.path.exists(CAMINHO_JSON):
        dados_iniciais = {"usuarios": [], "contatos": [], "agendamentos": []}
        salvar_dados(dados_iniciais)
        return dados_iniciais

    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados(dados):
    """Grava o dicionário completo de volta no banco.json."""
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def gerar_id(lista):
    """Gera um novo id incremental para uma lista de registros."""
    if not lista:
        return 1
    return max(item.get("id", 0) for item in lista) + 1


# ----------------------------
# ROTA 1: Página inicial (GET)
# ----------------------------
@app.route("/")
def inicio():
    dados = carregar_dados()

    # contador de visitas usando session (mantido conforme pedido)
    if "visitas" not in session:
        session["visitas"] = 1
    else:
        session["visitas"] += 1

    return render_template(
        "inicio.html",
        total_usuarios=len(dados["usuarios"]),
        visitas=session["visitas"]
    )


# ----------------------------
# ROTA 2: Cadastro de usuário -> CREATE (GET/POST)
# ----------------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        dados = carregar_dados()

        for usuario in dados["usuarios"]:
            if usuario["email"] == email:
                return render_template("cadastro.html", erro="Este e-mail já está cadastrado.")

        novo_usuario = {
            "id": gerar_id(dados["usuarios"]),
            "nome": nome,
            "email": email,
            "senha": senha
        }

        dados["usuarios"].append(novo_usuario)
        salvar_dados(dados)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


# ----------------------------
# ROTA 3: Login (GET/POST)
# ----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        dados = carregar_dados()

        for usuario in dados["usuarios"]:
            if usuario["email"] == email and usuario["senha"] == senha:
                session["usuario_id"] = usuario["id"]
                session["usuario_nome"] = usuario["nome"]
                return redirect(url_for("perfil"))

        return render_template("login.html", erro="E-mail ou senha inválidos.")

    return render_template("login.html")



# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("inicio"))



# Perfil do usuario logado
@app.route("/perfil")
def perfil():
    if "usuario_nome" not in session:
        return redirect(url_for("login"))

    dados = carregar_dados()
    meus_agendamentos = [
        a for a in dados["agendamentos"] if a.get("usuario_id") == session.get("usuario_id")
    ]

    return render_template(
        "perfil.html",
        nome=session["usuario_nome"],
        agendamentos=meus_agendamentos
    )



# Contato
@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        dados = carregar_dados()

        novo_contato = {
            "id": gerar_id(dados["contatos"]),
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "mensagem": request.form.get("mensagem")
        }

        dados["contatos"].append(novo_contato)
        salvar_dados(dados)

        return render_template("contato.html", sucesso=True)

    return render_template("contato.html")



# Agendamento
@app.route("/agendamento", methods=["GET", "POST"])
def agendamento():
    if "usuario_nome" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        dados = carregar_dados()

        novo_agendamento = {
            "id": gerar_id(dados["agendamentos"]),
            "usuario_id": session["usuario_id"],
            "paciente": session["usuario_nome"],
            "psicologo": request.form.get("psicologo"),
            "data": request.form.get("data"),
            "horario": request.form.get("horario")
        }

        dados["agendamentos"].append(novo_agendamento)
        salvar_dados(dados)

        return redirect(url_for("perfil"))

    return render_template("agendamento.html")



# Listar todos os agendamentos
@app.route("/agendamentos")
def agendamentos():
    dados = carregar_dados()
    return render_template("agendamentos.html", agendamentos=dados["agendamentos"])



# Editar agendamento
@app.route("/agendamento/editar/<int:id>", methods=["GET", "POST"])
def editar_agendamento(id):
    if "usuario_nome" not in session:
        return redirect(url_for("login"))

    dados = carregar_dados()
    agendamento_atual = next((a for a in dados["agendamentos"] if a["id"] == id), None)

    if agendamento_atual is None:
        return redirect(url_for("perfil"))

    if request.method == "POST":
        agendamento_atual["psicologo"] = request.form.get("psicologo")
        agendamento_atual["data"] = request.form.get("data")
        agendamento_atual["horario"] = request.form.get("horario")

        salvar_dados(dados)
        return redirect(url_for("perfil"))

    return render_template("editar_agendamento.html", agendamento=agendamento_atual)



# Excluir
@app.route("/agendamento/excluir/<int:id>")
def excluir_agendamento(id):
    if "usuario_nome" not in session:
        return redirect(url_for("login"))

    dados = carregar_dados()
    dados["agendamentos"] = [a for a in dados["agendamentos"] if a["id"] != id]
    salvar_dados(dados)

    return redirect(url_for("perfil"))



# Listar usuarios
@app.route("/usuarios")
def usuarios():
    dados = carregar_dados()
    return render_template("usuarios.html", usuarios=dados["usuarios"])


if __name__ == "__main__":
    app.run(debug=True)