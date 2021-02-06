from .settings import settings


def map_value(value, key):
    if isinstance(value, bool):
        return int(value)
    return value
