"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_assets import Environment

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        from .profile import profile
        from . home import home
        from . import routes
        from . import auth
        from .assets import compile_static_assets
        
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        
        
        # Create Database Models
        db.create_all()
        
        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)
      

        return app
