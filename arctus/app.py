import flask

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
    products = helpers.get_config('products')

    max_pc = products[0]
    max_storage = max_pc['stats']['storage']
    max_gpu = max_pc['stats']['gpu']
    max_cpu = max_pc['stats']['cpu']

    sort_key = flask.request.args.get('sort', 'price')
    products = sorted(products, key=lambda products: products[sort_key])

    for product in products:
        product['percentage'] = {}
        stats = product['stats']

        product['percentage']['storage'] = round(stats['storage'] / max_storage * 100)
        product['percentage']['gpu'] = round(stats['gpu'] / max_gpu * 100)
        product['percentage']['cpu'] = round(stats['cpu'] / max_cpu * 100)

        if product['name'].startswith('-HIDDEN- '):
            products.remove(product)

    return flask.render_template('shop/shop.html', title='Shop', products=products)

app.run(port=1313, debug=True)
