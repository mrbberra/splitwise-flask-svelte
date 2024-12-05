from flask import Flask, send_from_directory, session, redirect, url_for
import splitwise
from .lib import splitwise
from .blueprints import auth, api
from .blueprints.auth import login_required
import json
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = os.urandom(24).hex()
    if test_config is None:
       app.config.from_file('secrets.json', load=json.load)
    else:
        app.config.from_mapping(test_config)
    app.app_context().push()
    splitwise.get_splitwise()

    @app.route('/')
    def index():
      if 'access_token' in session:
        return redirect(url_for('client'))
      else:
        return redirect(url_for('auth.login'))

    # https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
    # Path for all the static files (compiled JS/CSS, etc.)
    @login_required
    @app.route('/client')
    def client():
      return send_from_directory('./client/dist', 'index.html')

    @login_required
    @app.route('/client/<path:path>')
    def client_internals(path):
      return send_from_directory('./client/dist', path)

    app.register_blueprint(auth.bp)
    app.register_blueprint(api.bp)
    return app
