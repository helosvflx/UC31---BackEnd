from flask import Flask, render_template, session, request

app = Flask(__name__)

app.secret_key = "123"

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contador', methods=['GET', 'POST'])
def contador():

    if 'contador' not in session:
        session['contador'] = 0

    if request.method == 'POST':
        session.pop('contador', None)
        session['contador'] = 0
    else:
        session['contador'] += 1

    return render_template('contador.html', contador=session['contador'])

if __name__ == '__main__':
    app.run(debug=True)