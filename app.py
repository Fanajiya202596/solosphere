from flask import Flask
from config import Config
from utils.db_init import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB
    init_db()

    # Register Blueprints
    from routes.subject_routes import subject_bp
    app.register_blueprint(subject_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)