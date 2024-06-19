from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://botdb_user:botdb_password@localhost:5432/botdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the deliveries model
class Delivery(db.Model):
    __tablename__ = 'deliveries'
    delivery_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
    delivery_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    received_by = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.factory_id'))

# Route to display deliveries from the last 10 days
@app.route("/")
def show_deliveries():
  return render_template('fournisseur.html')

if __name__ == "__main__":
    app.run(debug=True)
