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
    # Calculate the date 10 days ago from today
    ten_days_ago = datetime.now() - timedelta(days=10)
    
    # Query deliveries from the last 10 days
    recent_deliveries = Delivery.query.filter(Delivery.delivery_date >= ten_days_ago).order_by(Delivery.delivery_date.desc()).all()
    
    # Construct HTML response
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recent Deliveries</title>
        <style>
            table {
                text-align: center;
                width: 100%;
                border-collapse: collapse; 
                border: 1px solid;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <h1>Welcome to the Human-Bot Project</h1>
            <h2>Stock Service</h2>
            <h3>Recent Deliveries</h3>
            <table>
                <tr>
                    <th>Delivery ID</th>
                    <th>Supplier ID</th>
                    <th>Delivery Date</th>
                    <th>Quantity</th>
                    <th>Received By</th>
                    <th>Factory ID</th>
                </tr>
    '''

    for delivery in recent_deliveries:
        html_content += f'''
                <tr>
                    <td>{delivery.delivery_id}</td>
                    <td>{delivery.supplier_id}</td>
                    <td>{delivery.delivery_date}</td>
                    <td>{delivery.quantity}</td>
                    <td>{delivery.received_by}</td>
                    <td>{delivery.factory_id}</td>
                </tr>
        '''

    html_content += '''
            </table>
        </div>
    </body>
    </html>
    '''

    return html_content

if __name__ == "__main__":
    app.run(debug=True)
