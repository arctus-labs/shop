"""Main Arctus runner."""
import flask

from . import mail
from .. import helpers

accounts = flask.Blueprint('accounts', __name__)

@accounts.route('/account', methods=['GET', 'POST'])
def account_home():
    """Arctus home page."""
    if flask.request.method == 'POST':
        if flask.request.form.get('email') and flask.request.form.get('password'):
            mail.send(
                to=flask.request.form.get('email'),
                subject='Verify your Arctus account',
                html=flask.render_template(
                    'accounts/templates/verify.email.html',
                    url=''
                )
            )

        return flask.render_template('accounts/templates/create.html', title='Home')

    return flask.render_template('accounts/templates/create.html', title='Home')
