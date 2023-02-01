import secrets
import yaml

def get_config(name: str):
    with open(f'arctus/config/{name}.yml', 'r', encoding='utf8') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)

def token_generator() -> str:
    """Generate a random token."""
    return secrets.token_hex(32)
