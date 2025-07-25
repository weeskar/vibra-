from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('VIBRA_SECRET', 'clave-secreta-vibra')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vibra.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)

    # Importar y registrar blueprints
    from .routes.home import home_bp
    from .routes.auth import auth_bp
    from .routes.perfil import perfil_bp
    from .routes.match import match_bp
    from .routes.config import config_bp
    from vibra.routes.chakra import chakra_bp


    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(perfil_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(chakra_bp)

    # Validación de sesión (antes era @app.before_request)
    from .models import Usuario
    @app.before_request
    def validar_sesion():
        from flask import session
        user_id = session.get('usuario_id')
        if user_id and not Usuario.query.get(user_id):
            session.clear()

    return app