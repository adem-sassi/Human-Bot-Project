from flask import Flask

app = Flask(__name__)



@app.route("/")
def stock():
    return '''
    <div>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Stock service <h2>
    <h3>Lastest deliveries(10 days) -- Factory 1<h3>
    
    <h3>Lastest deliveries(10 days) -- Factory 2<h3>
    <div>
    '''
