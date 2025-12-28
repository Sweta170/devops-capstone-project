
# __init__.py
from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    
    # Security headers with Talisman
    Talisman(
        app,
        content_security_policy={
            'default-src': [
                "'self'"
            ],
            'img-src': [
                "'self'",
                'data:'
            ],
            'script-src': [
                "'self'"
            ]
        },
        force_https=True,
        strict_transport_security=True
    )
    
    # Import routes
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
