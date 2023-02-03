import sqlalchemy

from .. import db
from .. import app
from ..models import *

def already_exists(email):
    """Check if an email already exists in the database.
    """
    try:
        return bool(User.query.filter_by(email=email).first())
    except sqlalchemy.exc.OperationalError:
        return False
