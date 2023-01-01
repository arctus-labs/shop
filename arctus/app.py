import flask
import logging

app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARN)

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
