import helpers

best_pc = helpers.get_config('products')[0]['stats']

def process(data: dict):
    """Processes a product's data."""
    data['percentage'] = {}
    stats = data['stats']

    data['percentage']['storage'] = round(stats['storage'] / best_pc['storage'] * 100)
    data['percentage']['gpu'] = round(stats['gpu'] / best_pc['gpu'] * 100)
    data['percentage']['cpu'] = round(stats['cpu'] / best_pc['cpu'] * 100)

    return data

def list_all(sort_by: str='price', show_hidden: bool=False):
    """Returns a list of all products sorted by the given key."""

    products = helpers.get_config('products')
    products = sorted(products, key=lambda products: products[sort_by])

    for product in products:
        product = process(product)

        if product['name'].startswith('-HIDDEN- ') and not show_hidden:
            products.remove(product)

    return products

