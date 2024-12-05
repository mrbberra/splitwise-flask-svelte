from flask import Flask, send_from_directory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
      return send_from_directory('./client/dist', 'index.html')

    # https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
    # Path for all the static files (compiled JS/CSS, etc.)
    @app.route('/client/<path:path>')
    def assets(path):
      return send_from_directory('./client/dist', path)

    return app
