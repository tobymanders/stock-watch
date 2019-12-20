from flask import Flask
app = Flask(__name__)
from flaskapp import views
from flaskapp import main



# app.jinja_env.globals.update(format_time=format_time)
