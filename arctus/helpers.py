import json

def get_config(name: str):
    with open(f'arctus/config/{name}.json', 'r', encoding='utf8') as f:
        return json.load(f)

