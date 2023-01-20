"""Main Arctus runner."""
import flask

from .. import pcs
from .. import helpers

noctus = flask.Blueprint('noctus', __name__, template_folder='../')

@noctus.route('/')
def home():
    """Arctus home page."""

    return flask.render_template('noctus/templates/home.html', title='Home')

@noctus.route('/<path:subpath>')
def page_loader(subpath):
    """Loads pages from their directory."""

    pages = helpers.get_config('pages')
    print(subpath)

    if not subpath in pages:
        return flask.abort(404)

    return flask.render_template(f'noctus/templates/{subpath}.html', title=pages[subpath])

@noctus.route('/email')
def email():
    """Redirects to email address."""

    return flask.redirect('mailto:info@arctus.me')

@noctus.route('/support')
def support():
    """Support page redirects to email address."""

    return flask.redirect('/email')

@noctus.route('/shop')
def shop():
    """Shop page."""

    sort_key = flask.request.args.get('sort', 'price')
    invert_sort = flask.request.args.get('invert_sort', '0') == '1'

    try:
        products = pcs.list_all(sort_by=sort_key, invert_sort=invert_sort)
    except KeyError:
        return flask.abort(400)

    return flask.render_template('noctus/templates/shop/shop.html',
        title='Shop',
        products=products,
        sort_options=pcs.get_sort_options(sort_key),
        invert_sort=invert_sort
    )

@noctus.route('/shop/product/<product_id>')
def product(product_id):
    """Product page."""

    product = pcs.get(product_id)
    if not product:
        return flask.abort(404)

    return flask.render_template('noctus/templates/shop/product.html',
        title=product['name'],
        product=product
    )
