"""Main Arctus runner."""
import flask

from .. import helpers

accounts = flask.Blueprint('accounts', __name__)

@accounts.route('/account')
def account_home():
    """Arctus home page."""

    return flask.render_template('home.html', title='Home')
