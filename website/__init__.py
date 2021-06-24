from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqa
from os import path

db = sqa()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # encrypts sessiondata and cookies
    app.config['SECRET_KEY'] = 'mykey'
    # evaluates python code as a string
    app.config['SQLALCHEMY-DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import authÍ
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # defining schemas before database creation
    from .models import User, Note

    return app
    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')