from flask import Flask, render_template
from flask import request

import sys
sys.path.append('../src/')

import getresults


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello, World!"

@app.route('/index', methods=["GET", "POST"])
def index():
    url = request.args.get('zip_code')
    return render_template("input.html", preset_url=url)

@app.route('/output', methods=["GET", "POST"])
def table_output():
    # return url
    url = request.args.get('zip_code')

    results = getresults.main(url)
    return render_template("output.html", table=results)

if __name__ == "__main__":
    app.run(debug=True)
