from flask import Flask

app = Flask(__name__)



@app.route("/")
def rh():
    return '''
    <div>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Human Ressouces service<h2>
    <h3> Factory 1<h3>
    <h3> Factory 2<h3>
    <div>
    '''
