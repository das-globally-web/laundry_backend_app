# decorators.py
from functools import wraps
from django.shortcuts import redirect

def session_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'user' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
