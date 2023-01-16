import flask
import logging

import helpers

app = flask.Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

@app.context_processor
def injector():
    """Variables that are injected in all templates."""
    return dict(
        nav_links=helpers.get_config('nav'),
        socials=helpers.get_config('socials'),
        path=flask.request.path,
        links=helpers.get_config('footer-links').items(),
        url_args=flask.request.args
    )

@app.route('/')
def home():
    return flask.render_template('home.html', title='Home')

@app.errorhandler(404)
def error_404(error):
    return flask.render_template('error/404.html', title='404'), 404

@app.route('/<path:subpath>')
def page_loader(subpath):
    pages = helpers.get_config('pages')

    if not subpath in pages:
        return flask.abort(404)

    return flask.render_template(f'{subpath}.html', title=pages[subpath])

@app.route('/email')
def email():
    return flask.redirect('mailto:info@arctus.me')

@app.route('/support')
def support():
    return flask.redirect('/email')

@app.route('/shop')
def shop():
    return flask.render_template('shop/home.html', title='Shop', products=helpers.get_config('products'))

app.run(port=1313, debug=True)
