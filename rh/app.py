from flask  import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/human_bot'
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.factory_id'))

@app.route('/employees')
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
