from flask import Flask

app = Flask(__name__)



@app.route("/")
def rh():
    return '''
    <style>
    table {
    text-align: center;
    width: 100%;
    border-collapse: collapse; 
    border: 1px solid;
    }
    </style>

    <div style="text-align: center; ">
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Human Ressouces service<h2>
    <h3> Factory 1<h3>

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

    <h3> Factory 2<h3>

<table >
    <tr>
        <td>FirstName</td>
        <td>LastName</td>
        <td>Age</td>
        <td>Start Date</td>
        <td>End Date / is active</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td> </td>
        <td></td>
    </tr>
    </table>

    <div>
    '''
