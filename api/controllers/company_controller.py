from flask import request
from werkzeug.security import generate_password_hash
import services.company_service as company_service


def create_company():
    name, username, password = request.form.values()

    hashed_password = generate_password_hash(password)
    user = {
        'name': name,
        'username': username,
        'password': hashed_password
    }

    return company_service.create_company(user)


def get_company_by_id(company_id):
    return company_service.get_company_by_id(company_id)


def update_company_by_id(company_id):
    name = request.form.get('name')

    return company_service.update_company_by_id(company_id, name)


def delete_company_by_id(company_id):
    return company_service.delete_company_by_id(company_id)


def get_all_projects_by_company_id(company_id):
    return company_service.get_all_projects_by_company_id(company_id)


def get_employees_by_company_id(company_id):
    return company_service.get_employees_by_company_id(company_id)
