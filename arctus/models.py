from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model):
    """User model: username, email, password hash."""
    id = db.Column(db.Integer, primary_key=True)
    verify_token = db.Column(db.String(32), unique=True, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """Set the password hash for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the password hash for the user."""
        return check_password_hash(self.password_hash, password)
