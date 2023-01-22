"""Module managing the custom Flask application ("Flarc")."""

import os
import flask
import logging
import flask_wtf.csrf

from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

from . import helpers

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

class Flarc(flask.Flask):
    """Custom Flask application."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Jinja cleanup
        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True

        # Misc
        self.wsgi_app = ProxyFix(self.wsgi_app, x_proto=1)

        self.secret_key = os.urandom(24)
        self.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000 * 1000 # 1 GB
        self.config.from_mapping({
            "CACHE_TYPE": "SimpleCache",
            "DEBUG": True,
            "CACHE_DEFAULT_TIMEOUT": 300
        })

        # CSRF Protection
        self.csrf = flask_wtf.CSRFProtect(self)

        # Database
        self.db = SQLAlchemy()
        self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
        self.db.init_app(self)

        @self.context_processor
        def injector():
            """Variables that are injected in all templates."""
            return dict(
                nav_links=helpers.get_config('nav'),
                socials=helpers.get_config('socials'),
                path=flask.request.path,
                links=helpers.get_config('footer-links').items(),
                url_args=flask.request.args,
                user=flask.session.get('user', None),
        )

        @self.errorhandler(400)
        def error_400(error):
            """400 error page."""

            return flask.render_template('noctus/templates/error/400.html', title='400', message=error), 400

        @self.errorhandler(404)
        def error_404(*args, **kwargs):
            """404 error page."""

            return flask.render_template('noctus/templates/error/404.html', title='404'), 404

        @self.errorhandler(flask_wtf.csrf.CSRFError)
        def csrf_error(error):
            return flask.render_template('noctus/templates/error/400.html', title='400', message=f'CSRFError: {error}'), 400
