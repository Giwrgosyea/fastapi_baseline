from functools import wraps
from mongoengine import connect, disconnect
from ...config import get_settings

settings = get_settings()


def mongodb_access(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        connect(db=settings.mongo_database, host=settings.mongo_uri)
        res = f(*args, **kwargs)
        disconnect()
        return res

    return decorated
