from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Endpoint URL for the stock API
STOCK_API_URL = 'http://127.0.0.1:5002/api/stock/'

@app.route('/')
def index():
    factory_ids = [1, 2]  
    stock_data = {}

    for factory_id in factory_ids:
        api_url = f"{STOCK_API_URL}{factory_id}"
        response = requests.get(api_url)
        if response.status_code == 200:
            stock_data[factory_id] = response.json()['stock_quantity']
        else:
            stock_data[factory_id] = 'Error fetching data'

    # Render the HTML template with stock_data
    return render_template('stock.html', stock_data=stock_data)

if __name__ == '__main__':
    app.run(debug=True)
