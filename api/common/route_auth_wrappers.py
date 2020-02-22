from flask import session, jsonify
from functools import wraps
import controllers.project_controller as project_controller
import controllers.employee_controller as employee_controller


def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'company_id' in session:
            return f(session.get('company_id'), *args, **kwargs)

        return jsonify({'error': 'No session, user is not logged in'})

    return decorated


def project_owned_by_id(f):
    @wraps(f)
    def decorated(project_id, *args, **kwargs):
        if validate_project_owned_by_id:
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


def employee_owned_by_id(f):
    @wraps(f)
    def decorated(employee_id, *args, **kwargs):
        if validate_employee_owned_by_id:
            return f(employee_id, *args, **kwargs)

        return jsonify({'error': 'Protected route, access denied'})

    return decorated


def employee_and_project_owned_by_id(f):
    @wraps(f)
    def decorated(employee_id, project_id, *args, **kwargs):
        if validate_project_owned_by_id(project_id) and validate_employee_owned_by_id(employee_id):
            return f(employee_id, project_id, *args, **kwargs)

        return jsonify({'error': 'Protected route, access denied'})

    return decorated


def validate_project_owned_by_id(project_id):
    if 'company_id' in session:
        session_company_id = session.get('company_id')
        company_id = project_controller.get_company_id_by_project_id(project_id)
        return session_company_id == company_id

    return False


def validate_employee_owned_by_id(employee_id):
    if 'company_id' in session:
        session_company_id = session.get('company_id')
        company_id = employee_controller.get_company_id_by_employee_id(employee_id)
        return session_company_id == company_id

    return False
