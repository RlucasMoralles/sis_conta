# Sistema de Controle de Contas

Este projeto é um pequeno sistema de controle de despesas escrito em **Flask** utilizando **SQLite** como banco de dados. Ele permite cadastrar condições de pagamento, status e registrar despesas, exibindo todas as informações em uma página HTML simples.

## Funcionalidades principais
- Listar condições de pagamento e status cadastrados.
- Adicionar novas condições e status via formulários.
- Registrar despesas informando descrição, data, valor, condição e status.
- Visualizar todas as despesas registradas em uma tabela.
- API REST básica (em `app/`) para demonstrar cadastro de produtos com Flask-RESTful.

## Estrutura do projeto
```
app.py              # Aplicação Flask principal
model.py            # Classe de acesso ao banco de dados SQLite
app/                # Pacote com API REST de exemplo
templates/          # Templates HTML utilizados pela aplicação
env/                # Ambiente virtual com dependências (opcional)
database.db         # Base de dados SQLite utilizada pela aplicação
```

## Requisitos
- Python 3
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

As dependências podem ser instaladas com:
```bash
pip install Flask Flask-RESTful Flask-SQLAlchemy
```

## Como executar
1. Certifique-se de ter o Python instalado e as dependências listadas acima.
2. Execute o arquivo principal:
```bash
python app.py
```
3. Acesse `http://localhost:5000` no seu navegador para utilizar a aplicação.

A API REST disponível no pacote `app/` pode ser iniciada importando o módulo `app` e acessando as rotas definidas em `app/controller/reso_products.py`.

---
Este documento resume as funcionalidades básicas e a configuração inicial do projeto.
