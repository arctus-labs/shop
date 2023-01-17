import flask

import pcs
import flarc
import helpers

app = flarc.Flarc(__name__)

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
    """Arctus home page."""
    return flask.render_template('home.html', title='Home')

@app.errorhandler(404)
def error_404(*args, **kwargs):
    """404 error page."""
    return flask.render_template('error/404.html', title='404'), 404

@app.route('/<path:subpath>')
def page_loader(subpath):
    """Loads pages from their directory."""
    pages = helpers.get_config('pages')

    if not subpath in pages:
        return flask.abort(404)

    return flask.render_template(f'{subpath}.html', title=pages[subpath])

@app.route('/email')
def email():
    """Redirects to email address."""
    return flask.redirect('mailto:info@arctus.me')

@app.route('/support')
def support():
    """Support page redirects to email address."""
    return flask.redirect('/email')

@app.route('/shop')
def shop():
    """Shop page."""
    products = pcs.list_all(sort_by=flask.request.args.get('sort', 'price'))
    return flask.render_template('shop/shop.html', title='Shop', products=products)

app.run(port=1313, debug=True)
