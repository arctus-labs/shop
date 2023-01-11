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
        links=helpers.get_config('links').items(),
        url_args=flask.request.args
    )


@app.route('/')
def home():
    return flask.render_template('home.html', title='Home')

@app.route('/<path:subpath>')
def page_loader(subpath):
    pages = helpers.get_config('pages')
    print(pages)
    return flask.render_template(f'{subpath}.html', title=pages[subpath])

@app.route('/contact')
def contact():
    return flask.redirect('mailto:info@arctus.me')

app.run(port=1313, debug=True)
