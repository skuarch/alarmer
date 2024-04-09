import toml


with open('config/config.toml', 'r') as f:
    config = toml.load(f)


def get_config():
    return config
