"""Main Arctus runner."""
import flask

from . import mail
from . import system

from .. import db
from .. import helpers

accounts = flask.Blueprint('accounts', __name__)

@accounts.route('/verify/<token>')
def verify(token):
    """Verify an account."""
    # get the email from the token
    email = helpers.verify_token(token)

    # if the email is valid
    if email:
        # get the user from the database
        user = db.session.query(system.User).filter_by(email=email).first()

        # if the user exists
        if user:
            # set the user's verified status to true
            user.verified = True

            # commit the changes
            db.session.commit()

            # redirect to the login page
            return flask.redirect(flask.url_for('accounts.login'))

    # if the token is invalid
    return flask.render_template('accounts/templates/verify.html', title='Verify', error='Invalid token.')

@accounts.route('/account', methods=['GET', 'POST'])
def account_home():
    """Arctus home page."""
    if flask.request.method == 'POST':
        if flask.request.form.get('email') and flask.request.form.get('password'):
            # check if email already exists in the database
            # if it does, then we can't create an account
            if db.session.query(system.User).filter_by(email=flask.request.form.get('email')).first():
                return flask.render_template('accounts/templates/create.html', title='Home', error='An account with that email already exists.')

            # add the user to the database
            db.session.add(system.User(
                username=flask.request.form.get('username'),
                email=flask.request.form.get('email'),
                password=helpers.hash_password(flask.request.form.get('password'))
            ))

            # commit the changes
            db.session.commit()

            # send the verification email

            mail.send(
                to=flask.request.form.get('email'),
                subject='Verify your Arctus account',
                html=flask.render_template(
                    'accounts/templates/verify.email.html',
                    url=flask.url_for('accounts.verify', token=helpers.generate_token(flask.request.form.get('email')), _external=True)
                )
            )

        return flask.render_template('accounts/templates/create.html', title='Home')

    return flask.render_template('accounts/templates/create.html', title='Home')
