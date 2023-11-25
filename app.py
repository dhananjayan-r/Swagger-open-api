# app.py

from flask import Flask, render_template

app = Flask(__name__)


PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": "2022-10-08 09:15:10",
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": "2022-10-08 09:15:13",
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": "2022-10-08 09:15:27",
    }
}







@app.route("/app")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8060, debug=True)