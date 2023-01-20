"""Provides functions for getting and processing product data."""

from . import helpers

best_pc = helpers.get_config('products')[0]['stats']

def get_sort_options(sort_key: str) -> list:
    """Returns a list of sort options with the given key selected."""

    options = {
        'price': 'Preis',
        'storage': 'Speicherkapazität',
        'gpu': 'Grafikleistung',
        'cpu': 'Prozessorleistung',
        'value': 'Preis-Leistungs-Verhältnis'
    }

    sort_options = []
    for key, title in options.items():
        sort_options.append(
            {
                'key': key,
                'title': title,
                'is_selected': sort_key == key
            }
        )

    return sort_options

def calculate(stats: dict, key: str):
    """Calculates the performance percentage of a product's stats."""

    return round(stats[key] / best_pc[key] * 100)

def process(data: dict):
    """Processes a product's data by calculating all its performance percentages."""

    stats = data['stats']
    data['stats']['price'] = data['price']
    data['percentage'] = {
        'storage': calculate(stats, 'storage'),
        'gpu': calculate(stats, 'gpu'),
        'cpu': calculate(stats, 'cpu')
    }

    return data

def should_hide(product: dict, show_hidden: bool=False):
    """Returns whether a product should be hidden or not."""

    return product['name'].startswith('-HIDDEN- ') and not show_hidden

def list_all(sort_by: str='price', invert_sort: bool=False, show_hidden: bool=False):
    """Returns a list of all products sorted by the given key."""

    products = helpers.get_config('products')
    products = [process(p) for p in products if not should_hide(p, show_hidden)]
    products = sorted(products, key=lambda products: products['stats'][sort_by], reverse=invert_sort)

    return products

def get(product_id: str):
    """Returns a product by its ID."""

    products = helpers.get_config('products')
    products = [process(p) for p in products if not should_hide(p)]

    for product in products:
        if product['id'] == product_id:
            return product

    return None
