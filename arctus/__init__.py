import os
import flask
import logging
import flask_login
import flask_wtf.csrf
import flask_sqlalchemy

from werkzeug.middleware.proxy_fix import ProxyFix

from . import config
from . import helpers

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

db = flask_sqlalchemy.SQLAlchemy()
app = None

def create_app() -> flask.Flask:
    """Creates and prepares the Flask app.
    """
    global db
    global app

    # Jinja cleanup
    app = flask.Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # Misc
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)

    app.secret_key = os.urandom(24)
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000 * 1000 # 1 GB
    app.config['IMAGES_PATH'] = 'static/assets'
    app.config.from_mapping({
        "CACHE_TYPE": "SimpleCache",
        "DEBUG": True,
        "CACHE_DEFAULT_TIMEOUT": 300
    })

    # CSRF Protection
    app.csrf = flask_wtf.CSRFProtect(app)

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'

    db.init_app(app)

    login_manager = flask_login.LoginManager()
    login_manager.session_protection = 'strong'
    # login_manager.login_view = 'accounts.login'
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    @app.context_processor
    def injector():
        """Variables that are injected in all templates."""
        return dict(
            nav_links=helpers.get_config('nav'),
            socials=helpers.get_config('socials'),
            path=flask.request.path,
            links=helpers.get_config('footer-links').items(),
            url_args=flask.request.args,
            user=flask.session.get('user', None),
            web_address=config.WEB_ADDRESS,
            brand=config.BRAND,
            copyright=config.COPYRIGHT,
            support_email=config.SUPPORT_EMAIL,
            github_repo=config.GITHUB_REPO,
    )

    @app.errorhandler(400)
    def error_400(error):
        """400 error page."""

        return flask.render_template('noctus/templates/error/400.html', title='400', message=error), 400

    @app.errorhandler(404)
    def error_404(*args, **kwargs):
        """404 error page."""

        return flask.render_template('noctus/templates/error/404.html', title='404'), 404

    @app.errorhandler(flask_wtf.csrf.CSRFError)
    def csrf_error(error):
        return flask.render_template('noctus/templates/error/400.html', title='400', message=f'CSRFError: {error}'), 400

    @app.after_request
    def add_header(response):
        # improve performance using caching
        if response.headers['Content-Type'] == "image/png":
            response.headers['Cache-Control'] = 'must-revalidate, public, max-age=86400'
        else:
            response.headers['Cache-Control'] = 'must-revalidate, public, max-age=-1'
        return response

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from arctus.noctus.noctus import noctus
    from arctus.accounts.accounts import accounts

    app.register_blueprint(noctus)
    app.register_blueprint(accounts)

    return app

from . import pcs
from . import models
