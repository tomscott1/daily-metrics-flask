from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Flask-WTF csrf protection
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect()

from app import views, models  # avoid circular import error
