from flask import Flask

app = Flask(__name__)


@app.route("/")
def fournisseur():
    return '''
    <div>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Supplier Service <h2>
    <div>
    '''