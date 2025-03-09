from flask import Flask
# from App.routes.general_routes import general_bp
from App.routes.auth_routes import auth_bp,dashboard_bp
from App.config import Config
from flask_login import LoginManager
from App.models.user import User
from flask import Flask, redirect, url_for, flash,request
from flask_login import LoginManager
from App.db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        next_page = request.args.get('next')
        flash(Config.LOGIN_MESSAGE, Config.LOGIN_MESSAGE_CATEGORY)
        return redirect(url_for('auth_bp.login',next=next_page))


    # Initialize database
    init_db(app)

    @app.cli.command('seed')
    # Populate the database with some initial data
    def seed_db():
        from App.scripts.seeder import seed_database
        seed_database(app)
    @app.cli.command('make_db')
    # Populate the database with some initial data
    def make_db():
        from App.scripts.make_db import make_db
        make_db(app)
        



    # Register Blueprints
    # app.register_blueprint(general_bp)  # General routes
    # app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth routes with prefix
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    return app
