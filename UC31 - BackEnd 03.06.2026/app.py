from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/validacao', methods=['POST'])
def cadastro():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    cpf = request.form.get('cpf', '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso = request.form.get('curso', '').strip()
    idade = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '').strip()

    telefone = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    cpf = cpf.replace('.', '').replace('-', '')

    if not nome or len(nome) < 8:
        return "Nome inválido."

    if not email or '@' not in email or '.com' not in email:
        return "E-mail inválido."

    if len(telefone) != 11 or not telefone.isdigit():
        return "Telefone inválido."

    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido."

    if not cidade or len(cidade) < 3:
        return "Cidade inválida."

    if len(estado) != 2:
        return "Estado inválido."

    if not curso:
        return "Curso obrigatório."

    if not idade.isdigit() or int(idade) < 16:
        return "Idade inválida."

    if len(senha) < 8 or not any(caractere.isdigit() for caractere in senha):
        return "Senha muito fraca."

    return f"""
    <h1>Cadastro realizado com sucesso!</h1>

    Nome: {nome}<br>
    E-mail: {email}<br>
    Telefone: {telefone}<br>
    CPF: {cpf}<br>
    Cidade: {cidade}<br>
    Estado: {estado}<br>
    Curso: {curso}<br>
    Idade: {idade}
    """

if __name__ == '__main__':
    app.run(debug=True)