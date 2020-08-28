"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        from .profile import profile
        from .home import home
        
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)
      

        return app
