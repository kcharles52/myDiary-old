from flask import Flask
from config import app_configuration

def create_app(mode):
    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    app.config.from_object(app_configuration[mode])

    from api.views import app
    return app
