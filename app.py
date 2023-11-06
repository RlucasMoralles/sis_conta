from flask import Flask, render_template, request, redirect, url_for
from model import AppBD
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudgestao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

banco = AppBD()
banco.criarTabelas()
# Dados para inserir na tabela codicoes

#inserir condições padrão
descricao_condicoes = ["Pix", "Dinheiro", "Boleto Bancário", "Cartão de Crédito", "Cartão de Débito"]
banco.inserirCondicoesPadrao(descricao_condicoes)#israel melo

#inserir condições padrão
descricao_Status = ["Receita", "Receita Pendente", "Despesas Paga", "Despesas Pendente"]
banco.inserirStatusPadrao(descricao_Status)

@app.route('/')
def index():
    condicoes = banco.selectCondicoes()
    status = banco.selectStatus()
    despesas = banco.selecionarDespesas()
    return render_template('index.html', condicoes=condicoes, status=status, despesas=despesas)

@app.route('/adicionar_condicao', methods=['POST'])
def adicionar_condicao():
    if request.method == 'POST':
        nova_condicao = request.form['nova_condicao']
        banco.inserirCondicao(nova_condicao)
        return redirect(url_for('index'))

@app.route('/adicionar_status', methods=['POST'])
def adicionar_status():
    if request.method == 'POST':
        novo_status = request.form['novo_status']
        banco.inserirStatus(novo_status)
        return redirect(url_for('index'))

@app.route('/adicionar_despesa', methods=['POST'])    
def adicionar_despesa():
    if request.method == 'POST':
        descricao = request.form['descricao']
        data = request.form['data']
        valor = float(request.form['valor'])
        nome_condicao = request.form['condicao']
        nome_status = request.form['status']

        # Buscar IDs correspondentes ao nome da condição e do status no banco de dados
        id_condicao = banco.obter_id_condicao_por_nome(nome_condicao)
        id_status = banco.obter_id_status_por_nome(nome_status)

        # Inserir despesa com IDs correspondentes
        banco.inserirDespesa(descricao, data, valor, id_condicao, id_status)
        return redirect(url_for('index'))

"""# Página para adicionar novo usuário
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Página para editar usuário
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cur.fetchone()
    conn.close()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

# Página para deletar usuário
@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))"""

if __name__ == '__main__':
    app.run(debug=True)
