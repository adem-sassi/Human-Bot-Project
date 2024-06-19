from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://botdb_user:botdb_password@localhost:5432/botdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class Factory(db.Model):
    __tablename__ = 'factories'
    factory_id = db.Column(db.Integer, primary_key=True)
    factory_name = db.Column(db.String(100), nullable=False)
    employees = db.relationship('Employee', backref='factory', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.factory_id'), nullable=False)

@app.route("/")
def index():
    try:
        factories = Factory.query.all()
    except Exception as e:
        app.logger.error(f"Error querying factories: {e}")
        return "An error occurred while fetching the data."
    return render_template('rh.html')

if __name__ == "__main__":
    app.run(debug=True)
