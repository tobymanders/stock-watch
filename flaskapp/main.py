from flask import Flask, render_template
from flask import request

import sys
sys.path.append('../src/')

import getresults


app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     return "Hello, World!"

@app.route('/', methods=["GET", "POST"])
def index():
    url = request.args.get('zip_code')
    product = request.args.get('Product')
    return render_template("input.html", preset_url=url, product=product)

@app.route('/output', methods=["GET", "POST"])
def table_output():
    # return url
    zipcode = request.args.get('location')
    product = request.args.get('Product')
    results = getresults.main(zipcode)
    return render_template("output.html", table=results, product=product)

if __name__ == "__main__":
    app.run(debug=True)
