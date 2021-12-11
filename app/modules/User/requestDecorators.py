from functools import wraps

from flask import request, abort, redirect, url_for


def onlyRegistered(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if request.ctx.get('user') is None:
            return redirect(url_for('homeRoute', language=request.ctx['language']))
        if not request.ctx['user']['is_logged_in']:
            return redirect(url_for('homeRoute', language=request.ctx['language']))
        return f(*args, **kwargs)
    return decoratedFunction