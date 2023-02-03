import flask_login
import werkzeug.security

from . import db
from datetime import datetime

class User(db.Model, flask_login.UserMixin):
    """User model: username, email, password hash.
    """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    verification_token = db.Column(db.String(32), unique=True, nullable=True)

    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    creation_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)#
    last_login_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def set_password(self, password: str) -> None:
        """Set the password hash for the user.
        """
        werkzeug.security.generate_password_hash(password, method='pbkdf2:sha512', salt_length=32)

    def check_password(self, password: str) -> bool:
        """Check if the given plaintext password matches its hash .
        """
        return werkzeug.security.check_password_hash(self.password_hash, password)
