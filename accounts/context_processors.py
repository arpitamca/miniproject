def user_name(request):
    """Expose logged-in user's name from session to all templates as `name`.

    This project stores the name in `request.session['user_name']` at login.
    """
    try:
        return {'name': request.session.get('user_name')}
    except Exception:
        return {'name': None}
