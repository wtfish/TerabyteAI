from flask import Flask
# from App.routes.general_routes import general_bp
from App.routes.auth_routes import auth_bp
from App.config import Config
from App.db import init_db
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db(app)

    # Register Blueprints
    # app.register_blueprint(general_bp)  # General routes
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth routes with prefix

    return app
