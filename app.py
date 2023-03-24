import json
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    with open("flight_details.json") as f:
        flight_details = json.load(f)
    return render_template(
        "index.html",
        flight_details=flight_details
    )

app.add_url_rule('/', 'index', index)