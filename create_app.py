# create_app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import tenseal as ts
import os



# Instanciar SQLAlchemy y Migrate
db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-only-change-me')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://p2p:local-db-only@db/p2p'
    )
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Desactivar caché de archivos estáticos

    # Inicializar las extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    return app
