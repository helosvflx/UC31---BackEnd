from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    if request.method == 'POST':
        nome = request.form.get('Nome')
        email = request.form.get('email')

    return "{} e {}".format(nome, email)

if __name__ == '__main__':
    app.run(debug=True)
