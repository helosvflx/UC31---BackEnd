from flask import Flask, render_template_string, request, redirect, url_for, flash, session

app = Flask(_name_)
app.config['SECRET_KEY'] = 'minha-chave-2025'

USUARIOS = [
    {
        'id': 1,
        'nome': 'Ana Silva',
        'email': 'ana@email.com',
        'senha_hash': generate_password_hash('senha123')
    },
    {
        'id': 2,
        'nome': 'Carlos Lima',
        'email': 'carlos@email.com',
        'senha_hash': generate_password_hash('abc456')
    }
]

def buscar_usuario(email):
    for u in USUARIOS:
        if u['email'] == email:
            return u
    return None

#Rota: login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '').strip()
        
        usuario = buscar_usuario(email)
        
        if not usuario:
            flash('E-mail não encontrado.', 'erro')
            return redirect(url_for('login'))
            
        if not check_password_hash(usuario['senha_hash'], senha):
            flash('Senha incorreta.', 'erro')
            return redirect(url_for('login'))
            
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        
        flash(f"Bem-vindo, {usuario['nome']}!", 'sucesso')
        return redirect(url_for('painel'))
        
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
        <h1>Login</h1>
        <form method="POST">
            <input type="email" name="email" placeholder="E-mail" required>
            <input type="password" name="senha" placeholder="Senha" required>
            <button type="submit">Entrar</button>
        </form>
        </body>
        </html>
    ''')

#Rota: painel
@app.route('/painel')
def painel():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    nome = session['usuario_nome']
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Olá, {{ nome }}!</h1>
            <a href="/logout">Sair</a>
        </body>
        </html>
    ''', nome=nome)

#Rota: logout
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('login'))

if name == '__main__':
    app.run(debug=True)