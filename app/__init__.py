from flask import Flask
from config import Config
from .extensions import db, migrate
from .controllers.region_controller import region_controller
from .controllers.city_controller import city_controller
from .controllers.auth_controller import auth_controller

def create_app():
    # init app
    app = Flask(__name__)

    # config
    app.config.from_object(Config)

    # init db
    db.init_app(app)

    # init migration
    migrate.init_app(app, db)
    
    # add controllers
    app.register_blueprint(region_controller, url_prefix='/api')
    app.register_blueprint(city_controller, url_prefix='/api')
    app.register_blueprint(auth_controller, url_prefix='/api')

    return app