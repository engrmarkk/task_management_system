from extensions import db, jwt, migrate, socketio
from flask import Flask
from models import User, Task
from config import config_dict
from endpoints import UserBlueprint, AuthBlueprint
import logging


BASE_URL = "/api/v1"

def create_app(config_name="development"):
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    app.config.from_object(config_dict[config_name])

    db.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            db=db,
            User=User,
            Task=Task,
        )

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_payload):
        identity = jwt_payload["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    # register the blueprint
    app.register_blueprint(AuthBlueprint, url_prefix=f"{BASE_URL}/auth")
    app.register_blueprint(UserBlueprint, url_prefix=f"{BASE_URL}/user")

    return app
