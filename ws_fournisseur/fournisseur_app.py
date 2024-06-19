from flask import Flask

app = Flask(__name__)

@app.route("/menu")
def menu():
    return '''
    <div>
    <a href='http://127.0.0.1:5000/'>Home<a>
    <a href='http://127.0.0.1:5000/human-ressources'>Human Resources<a>
    <a href='http://127.0.0.1:5000/stock'>Stock<a>
    <a href='http://127.0.0.1:5000/supplier'>Supplier<a>
    <div>
    '''

@app.route("/")
def home():
    return '''
    <div>
    <a href='http://127.0.0.1:5000/menu'>MENU<a>
    <h1>Welcome to the Human-Bot Project</h1>
    <div>
    '''

@app.route("/human-ressources")
def hr():
    return '''
    <div>
    <a href='http://127.0.0.1:5000/menu'>MENU<a>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Human Ressouces service<h2>
    <h3> Factory 1<h3>
    <h3> Factory 2<h3>
    <div>
    '''

@app.route("/stock")
def stock():
    return '''
    <div>
    <a href='http://127.0.0.1:5000/menu'>MENU<a>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Stock service <h2>
    <h3>Lastest deliveries(10 days) -- Factory 1<h3>
    
    <h3>Lastest deliveries(10 days) -- Factory 2<h3>
    <div>
    '''

@app.route("/supplier")
def supplier():
    return '''
    <div>
    <a href='http://127.0.0.1:5000/menu'>MENU<a>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Supplier Service <h2>
    <div>
    '''