from functools import wraps

from flask import abort, redirect, request, url_for


def onlyRegistered(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if request.ctx.get('user') is None:
            return redirect(url_for('homeBlueprint.homeRoute', language=g.current_language.code))
        if not request.ctx['user']['is_logged_in']:
            return redirect(url_for('homeBlueprint.homeRoute', language=g.current_language.code))
        return f(*args, **kwargs)
    return decoratedFunction
