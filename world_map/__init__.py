from flask import flash, Flask, jsonify, render_template, request
from os import environ
from .database import get_people

app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
app.url_map.strict_slashes = False

@app.route('/')
def index():
    return render_template(
        'index.html', google_maps_api_key = environ['GOOGLE_MAPS_API_KEY']
    )

@app.route('/people')
def people():
    return jsonify(list(get_people()))