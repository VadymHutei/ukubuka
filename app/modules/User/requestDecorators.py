from functools import wraps


def onlyRegistered(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        return f(*args, **kwargs)
    return decoratedFunction
