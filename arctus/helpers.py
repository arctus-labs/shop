import yaml
import secrets
import werkzeug.security

def get_config(name: str):
    """Gets a config file.
    """
    with open(f'arctus/config/{name}.yml', 'r', encoding='utf8') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)

def generate_token() -> str:
    """Generate a random token.
    """
    return secrets.token_hex(32)
