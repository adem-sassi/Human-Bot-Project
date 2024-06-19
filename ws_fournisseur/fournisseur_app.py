from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://botdb_user:botdb_password@localhost:5432/botdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    delivery_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    delivery_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    received_by = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.factory_id'))

@app.route("/")
def show_deliveries():
    # For demonstration purposes, let's simulate some deliveries
    deliveries = [
        {'delivery_id': 1, 'supplier_name': 'Supplier A', 'delivery_date': datetime.now().date(), 'quantity': 100, 'employee_name': 'John Doe', 'factory_name': 'Factory X'},
        {'delivery_id': 2, 'supplier_name': 'Supplier B', 'delivery_date': datetime.now().date(), 'quantity': 150, 'employee_name': 'Jane Smith', 'factory_name': 'Factory Y'}
    ]

    return render_template('fournisseur.html', deliveries=deliveries)

if __name__ == "__main__":
    app.run(debug=True)
