from flask import Flask
from .controllers.region_controller import region_controller
from .controllers.city_controller import city_controller

def create_app():
    # int app
    app = Flask(__name__)

    # add controllers
    app.register_blueprint(region_controller, url_prefix='/api')
    app.register_blueprint(city_controller, url_prefix='/api')

    return app