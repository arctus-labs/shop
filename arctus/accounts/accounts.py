"""Main Arctus runner."""
import flask
import flask_login

from . import mail
from . import system

from .. import db
from .. import config
from .. import helpers

from ..models import *

accounts = flask.Blueprint('accounts', __name__)

@accounts.route('/account', methods=['GET', 'POST'])
def account_home():
    """Arctus home page.
    """
    if flask.request.method == 'POST':
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')

        if email and password:
            # check if email already exists in the database
            # if it does, then we can't create an account
            if system.already_exists(email):
                error_message = 'That email is already in use.'
                return flask.render_template('accounts/templates/create.html', title='Home', error=error_message)

            # add the user to the database
            user = User(
                email=email,
                username='',
                verification_token=helpers.generate_token()
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            # send the verification email
            mail.send(
                to=email,
                subject='Verify your Arctus account',
                html=flask.render_template(
                    'accounts/templates/verify.email.html',
                    url=f'{config.WEB_ADDRESS}/verify/'
                )
            )

            print('Account created successfully.')

        return flask.render_template('accounts/templates/create.html', title='Home')

    return flask.render_template('accounts/templates/create.html', title='Home')
