from flask import Flask, render_template, request, jsonify
from testing.q2q3 import create_table #update when folder name changes
import os

app = Flask(__name__)  #static_url_path='/static'

@app.route('/')

def index():
    return render_template('forecast.html')

@app.route('/forecast', method=['POST']) #check 

def run_script(): 

    consumable = request.form.get('consumable_name')
    result = create_table(consumable)
    return jsonify(result = result)
   # return render_template('forecast.html')

if __name__ == '__main__':
    app.run(debug=True)

