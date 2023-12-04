from flask import Flask, render_template, request, jsonify
#from q2q3 import create_table #update when folder name changes
from q2q3_food import create_table_food
from q2q3_oxygen import create_table_oxygen
from q2q3_water import create_table_water
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
    if consumable == 'Water':
        #table_data = create_table_water(consumable)
        #return render_template('forecast.html', table_data=table_data, consumable=consumable)
        info = create_table_water(consumable)
        table_d = info[0]
        g_date = info[1]
        greatest_qty = info[2]
        greatest_date = f'Date with highest consumable amount: {g_date}'
        qty = f'The greatest amount of consumable needed: {greatest_qty}'
        table_data = table_d.to_html(index=False)
        return render_template('forecast.html', table_data=table_data,
                                consumable=consumable, greatest_date=greatest_date,
                                qty=qty)
    elif consumable == 'Oxygen':
        #table_data = create_table_oxygen(consumable)
        #return render_template('forecast.html', table_data=table_data, consumable=consumable)
        info = create_table_oxygen(consumable)
        table_d = info[0]
        g_date = info[1]
        greatest_qty = info[2]
        greatest_date = f'Date with highest consumable amount: {g_date}'
        qty = f'The greatest amount of consumable needed: {greatest_qty}'
        table_data = table_d.to_html(index=False)
        return render_template('forecast.html', table_data=table_data,
                                consumable=consumable, greatest_date=greatest_date,
                                qty=qty)
    elif consumable == 'US Food BOBs':
        #table_data = create_table_food(consumable)
        info = create_table_food(consumable)
        table_d = info[0]
        g_date = info[1]
        greatest_qty = info[2]
        greatest_date = f'Date with highest consumable amount: {g_date}'
        qty = f'The greatest amount of consumable needed: {greatest_qty}'
        table_data = table_d.to_html(index=False)
        return render_template('forecast.html', table_data=table_data,
                                consumable=consumable, greatest_date=greatest_date,
                                qty=qty)



if __name__ == '__main__':
    app.run(debug=True)

