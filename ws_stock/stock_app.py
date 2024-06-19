from flask import Flask

app = Flask(__name__)



@app.route("/")
def stock():
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

    <div id="container">
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Stock service <h2>
    <h3>Lastest deliveries(10 days) -- Factory 1<h3>
    
    <table>
    <tr>
        <td>FirstName</td>
        <td>LastName</td>
        <td>Age</td>
        <td>Start Date</td>
        <td>End Date / is active</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4 </td>
        <td>5</td>
    </tr>
    </table>


    <div>
    '''
