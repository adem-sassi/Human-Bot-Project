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

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Human Resources</title>
        <style>
            table {
                text-align: center;
                width: 100%;
                border-collapse: collapse; 
                border: 1px solid;
            }

            #container{
                text-align: center;
                width: 100%;
            }

            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <h1>Welcome to the Human-Bot Project</h1>
    '''

    for factory in factories:
        html += f'''
            <h2>{factory.factory_name}</h2>
            <table>
                <tr>
                    <th>FirstName</th>
                    <th>LastName</th>
                    <th>Age</th>
                    <th>Start Date</th>
                    <th>End Date / is active</th>
                </tr>
        '''

        for employee in factory.employees:
            html += f'''
                <tr>
                    <td>{employee.firstname}</td>
                    <td>{employee.lastname}</td>
                    <td>{employee.age}</td>
                    <td>{employee.start_date}</td>
                    <td>{employee.end_date if employee.end_date else '/'}</td>
                    <td>{"Active" if employee.is_active else "Inactive"}</td>
                </tr>
            '''

        html += '''
            </table>
        '''

    html += '''
        </div>
    </body>
    </html>
    '''

    return html

if __name__ == "__main__":
    app.run(debug=True)
