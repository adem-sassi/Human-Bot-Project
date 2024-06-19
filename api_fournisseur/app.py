from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://botdb_user:botdb_password@localhost:5432/botdb'
db = SQLAlchemy(app)

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    delivery_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    delivery_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    received_by = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.factory_id'))

@app.route('/api/stock/<int:factory_id>', methods=['GET'])
def get_stock(factory_id):
    stock_quantity = db.session.query(db.func.sum(Delivery.quantity)).filter(Delivery.factory_id == factory_id).scalar()
    return jsonify({'factory_id': factory_id, 'stock_quantity': stock_quantity})

if __name__ == '__main__':
    app.run(debug=True)
