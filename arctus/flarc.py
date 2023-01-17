import os
import flask
import logging

from werkzeug.middleware.proxy_fix import ProxyFix

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

class Flarc(flask.Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.secret_key = os.urandom(24)
        self.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000 * 1000 # 1 GB

        self.jinja_env.trim_blocks = True
        self.jinja_env.lstrip_blocks = True

        self.wsgi_app = ProxyFix(self.wsgi_app, x_proto=1)

        self.config.from_mapping({
            "CACHE_TYPE": "SimpleCache",
            "DEBUG": True,
            "CACHE_DEFAULT_TIMEOUT": 300
        })
