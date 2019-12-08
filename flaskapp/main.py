from flask import Flask, render_template
from flask import request

import sys
sys.path.append('../src/')

import getresults


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    url = request.args.get('zip_code')
    return render_template("input.html", preset_url=url)

@app.route('/no_results')
def no_results():
    return "<h1>No Results!</h1>"

@app.route('/output', methods=["GET", "POST"])
def table_output():
    # return url
    zipcode = request.args.get('location')

    results = getresults.main(zipcode)
    return render_template("output.html", table=results)

if __name__ == "__main__":
    app.run(debug=True)
