from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def formulario():
    return render_template('index.html')


@app.route('/validacao', methods=['POST'])
def cadastro():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email','').strip().lower()
    cidade = request.form.get('cidade','').strip().title()

    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Cidade: {cidade}<br>
    """


if __name__ == '__main__':
    app.run(debug=True)