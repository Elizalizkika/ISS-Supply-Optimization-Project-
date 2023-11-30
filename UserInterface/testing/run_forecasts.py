from flask import Flask, render_template
import os

app = Flask(__name__, static_url_path='/static')  

@app.route('/forecast')
def forecast(): 
    return render_template('forecast.html')
#more to be added in order to retrieve algo ouput 

if __name__ == '__main__':
    app.run(debug=True)

