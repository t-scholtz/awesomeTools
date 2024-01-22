from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import PathLike

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = 'static/files'
    
    db.init_app(app)

    from .views import views
    from .pasteBin import pasteBin
    from .fileConverter import fileConverter

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(pasteBin, url_prefix='/')
    app.register_blueprint(fileConverter, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


