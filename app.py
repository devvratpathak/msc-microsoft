from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

app.run(port = 5000,debug=True)
