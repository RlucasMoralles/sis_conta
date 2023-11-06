from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models.products import Products
with app.app_context(): #garantir que as tabelas estejam prontas para uso antes de executar a aplicação Flask.
    db.create_all()

from app.controller.reso_products import Index, ProductCreate
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(ProductCreate, '/criar')
'''@app.route("/")
def index():
    return render_template("index.html")'''
#"<h1> Minha aplicação em Flask </h1>"