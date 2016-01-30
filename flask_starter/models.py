from flask_starter import app, db
from flask_starter.logs import logger, syslog, loglevel
import datetime
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True, index=True)
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

