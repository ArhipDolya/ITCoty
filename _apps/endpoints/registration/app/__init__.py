from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from _apps.endpoints.registration.models import User, UserActivation, PasswordReset

with app.app_context():
    db.create_all()
    print('DataBase created')


from _apps.endpoints.registration.app import views
from _apps.endpoints.registration.app import registration

