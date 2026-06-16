from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "123456"

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    erro = ""

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario and senha:
            session['logado'] = True
            session['usuario'] = usuario

            return redirect(url_for('dashboard'))

        else:
            erro = "Preencha todos os campos."

    return render_template('login.html', erro=erro)


@app.route('/dashboard')
def dashboard():

    if not session.get('logado'):
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        usuario=session.get('usuario')
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)