import json
import flask
import logging

app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

def get_nav():
    with open('arctus/config/nav.json', 'r', encoding='utf8') as f:
        return json.load(f)

@app.context_processor
def injector():
    return dict(nav_links=get_nav())

@app.route('/')
def index():
    return flask.redirect('/shop')

@app.route('/shop')
def shop():
    return flask.render_template('home.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/cart')
def cart():
    return flask.render_template('cart.html')

app.run(port=1313, debug=True)
