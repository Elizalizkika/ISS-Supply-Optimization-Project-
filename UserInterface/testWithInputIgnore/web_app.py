#trying to connect user input with algo UNFINISHED 

from flask import Flask, request, render_template
import UserInterface.testWithInputIgnore.water_us_copy as water_us_copy


app = Flask(__name__)

@app.route("/")
#to be used for usr input
#@app.route("/", methods=["GET", "POST"])

def run_forecast_water():
    result = None

    if request.method == "POST":
        # if submitted process data
        user_input_date = request.form.get("date")
        result = water_us_copy.py.algo(user_input_date)
        #need to make part of water us a function to be called on 

    return render_template("predictions.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
