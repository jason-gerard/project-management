from flask import request, jsonify
import services.employee_service as employee_service
import services.project_service as project_services


def create_employee(company_id):
    name = request.form.get('name')

    return employee_service.create_employee(company_id, name)


def get_employee_by_id(employee_id):
    return employee_service.get_employee_by_id(employee_id)


def update_employee_by_id(employee_id):
    name = request.form.get('name')

    return employee_service.update_employee_by_id(employee_id, name)


def delete_employee_by_id(employee_id):
    return employee_service.delete_employee_by_id(employee_id)


def get_company_id_by_employee_id(employee_id):
    employee = employee_service.get_employee_by_id(employee_id)
    return employee['company_id']


def add_employee_to_project(employee_id, project_id):
    return employee_service.add_employee_to_project(employee_id, project_id)


def get_projects_by_employee_id(employee_id):
    project_relations = employee_service.get_projects_by_employee_id(employee_id)
    project_ids = [relation['project_id'] for relation in project_relations]
    return jsonify(list(map(project_services.get_project_by_id, project_ids)))
