from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello, World!"

@app.route('/index', methods=["GET", "POST"])
def index():
    url = request.args.get('youtube_url')
    return render_template("input.html", preset_url=url)

@app.route('/output', methods=["GET", "POST"])
def chord_output():
    # return url
    url = request.args.get('youtube_url')
    urlint = int(url)
    return render_template("output.html", video=url)
    # video_code = url[32:]
    #
    # model_path = 'xgb_multifinal'
    # lr_predict.predict(url, model_path, f"{video_code}", 0.5, 24.5, 7, 1,
    #                     'Models/', 'Results/', 3)

if __name__ == "__main__":
    app.run(debug=True)
