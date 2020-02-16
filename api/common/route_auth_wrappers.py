from flask import session, jsonify
from functools import wraps
import controllers.project_controller as project_controller


def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'company_id' in session:
            return f(session['company_id'], *args, **kwargs)

        return jsonify({'error': 'No session, user is not logged in'})

    return decorated


def project_owned_by_id(f):
    @wraps(f)
    def decorated(project_id, *args, **kwargs):
        if 'company_id' in session:
            session_company_id = session['company_id']
            company_id = project_controller.get_company_id_by_project_id(project_id)

            if session_company_id == company_id:
                return f(project_id, *args, **kwargs)

        return jsonify({'error': 'Protected route, access denied'})

    return decorated


def company_owned_by_id(f):
    @wraps(f)
    def decorated(company_id, *args, **kwargs):
        if int(session.get('company_id')) == int(company_id):
            return f(company_id, *args, **kwargs)

        return jsonify({'error': 'Protected route, access denied'})

    return decorated
