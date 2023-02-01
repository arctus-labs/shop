from .. import db
from .. import app
from .. import models

with app.app_context():
    db.session.add(models.User(username='admin', email='admin@arctus.me'))
