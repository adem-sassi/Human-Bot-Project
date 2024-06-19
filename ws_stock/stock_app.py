from flask import Flask

app = Flask(__name__)



@app.route("/")
def stock():
    return '''
    <div>
    <h1>Welcome to the Human-Bot Project</h1>
    <h2> Stock service <h2>
    <h3>Lastest deliveries(10 days) -- Factory 1<h3>
    
    <table>
    <tr>
        <td>&nbsp;</td>
        <td>&nbsp;</td>
    </tr>
    <tr>
        <td>Race</td>
        <td>Jack Russell</td>
       
    </tr>
    <tr>
        <td>Age</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Propriétaire</td>
        <td>Belle-mère</td>
    </tr>
    <tr>
        <td>Habitudes alimentaires</td>
        <td>Mange tous les restes</td>
    </tr>
    </table>
    <h3>Lastest deliveries(10 days) -- Factory 2<h3>
    
    <table>
    <tr>
        <td>Race</td>
        <td>Jack Russell</td>
       
    </tr>
    <tr>
        <td>Age</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Propriétaire</td>
        <td>Belle-mère</td>
    </tr>
    <tr>
        <td>Habitudes alimentaires</td>
        <td>Mange tous les restes</td>
    </tr>
    </table>
    <div>
    '''
