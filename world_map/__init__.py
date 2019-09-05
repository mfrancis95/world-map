from flask import flash, Flask, jsonify, render_template, request, session
from os import environ
from flask_pyoidc.provider_configuration import *
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from .database import get_people, update_position
from .geocoding import geocode

app = Flask(__name__)
app.config.update(
    SECRET_KEY = environ['SECRET_KEY'], SERVER_NAME = environ['SERVER_NAME']
)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
app.url_map.strict_slashes = False

_config = ProviderConfiguration(
    environ['OIDC_ISSUER'],
    client_metadata = ClientMetadata(
        environ['OIDC_CLIENT_ID'], environ['OIDC_CLIENT_SECRET']
    )
)
_auth = OIDCAuthentication({'default': _config}, app)

@app.route('/')
@_auth.oidc_auth('default')
def index():
    return render_template(
        'index.html', google_maps_api_key = environ['GOOGLE_MAPS_API_KEY']
    )

@app.route('/people')
@_auth.oidc_auth('default')
def people():
    return jsonify(list(get_people()))

@app.route('/position', methods = ['POST'])
@_auth.oidc_auth('default')
def position():
    return jsonify(update_position(
        session['userinfo']['preferred_username'],
        geocode(str(request.get_data()))
    ))