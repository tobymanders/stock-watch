from flask import Flask, render_template
from flask import request

import sys
sys.path.append('../src/')

import getresults


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    url = request.args.get('zip_code')
    product = request.args.get('Product')
    return render_template("input.html", preset_url=url, product=product)

@app.route('/no_results')
def no_results():
    return "<h1>No Results!</h1>"

@app.route('/output', methods=["GET", "POST"])
def table_output():
    # return url
    zipcode = request.args.get('location')
    # product = request.args.get('Product')
    product = "AirPods" # TODO: CHANGE BACK TO THE ARG INPUT
    results = getresults.main(zipcode, product)
    num_results = len(results)
    # render_template("output.html", table=results, product=product)
    return render_template("output.html", table=results, num_results=num_results)

if __name__ == "__main__":
    app.run(debug=True)
