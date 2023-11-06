from app import db
class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement':True}
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __init__(self,name,price):
        self.name = name
        self.price = price

    
    def json(self):
        return {
            'name': self.name,
            'price': self.price
        }
     
    def save_products(self, name, price): #salvar a instancia no banco de dados
        try:
            add_banco = Products(name, price)
            db.session.add(add_banco) #adicionar a instância
            db.session.commit() #confirma
        except Exception as e: #se a -operação de salvar falhas, cai na exceção
            print(e)