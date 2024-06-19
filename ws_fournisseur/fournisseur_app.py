from flask import Flask

app = Flask(__name__)


@app.route("/")
def fournisseur():
    return '''
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

    <div  id="container">
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Supplier Service <h2>
    <h3>delivery last 10 days<h3>
    <table>
    <tr>
        <td>Delivery Id</td>
        <td>Supplier Name</td>
        <td>Delivery Date</td>
        <td>Quantity</td>
        <td>Employee</td>
        <td>Factory Name</td>

    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4 </td>
        <td>5</td>
        <td>6</td>
    </tr>
    </table>

    <div>
    '''