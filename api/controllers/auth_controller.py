from flask import request, session
from werkzeug.security import check_password_hash
import services.company_service as company_service


def sign_in():
    username = request.form['username']
    password = request.form['password']

    selected_user = company_service.get_company_by_username(username)

    if selected_user:
        is_authenticated = (check_password_hash(selected_user['password'], password) and
                            selected_user['username'] == username)

        if is_authenticated:
            session['company_id'] = selected_user['id']
            return {
                'msg': f'{username} is now signed in'
            }

    return {
        'error': 'user is not authenticated'
    }


def sign_out():
    if 'company_id' in session:
        session.pop('company_id', None)

        return {
            'msg': 'User is now signed out'
        }

    return {
        'err': 'No user to sign out'
    }
