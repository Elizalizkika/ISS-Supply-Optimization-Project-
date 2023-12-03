from flask import Flask, render_template, request, jsonify
from q2q3 import create_table #update when folder name changes
import pandas as pd
import os

#app = Flask(__name__)  
app = Flask(__name__, static_url_path='/static')

@app.route('/')

def index():
    return render_template('forecast.html')

@app.route('/run_script', methods=['POST']) #METHODS WITH AN S

def run_script(): #name of this function is where route goes
    #consumable = request.form.get('consumable_name')
    consumable = request.form['consumable_name']

    print(f"Consumable selected: {consumable}")
    table_data = create_table(consumable)
    return render_template('forecast.html', table_data=table_data)



if __name__ == '__main__':
    app.run(debug=True)

