from flask import request, jsonify
import services.project_service as project_service
import services.company_service as company_service
import services.employee_service as employee_service


def create_project(company_id):
    name = request.form.get('name')
    cost = request.form.get('cost')
    parent_project_id = request.form.get('parent_project_id')
    employee_ids = request.form.getlist('employees')

    res = project_service.create_project(name, cost, company_id, parent_project_id or 'null')

    project_id = res[0]['id']
    [employee_service.add_employee_to_project(int(employee_id), project_id) for employee_id in employee_ids]

    return res


def get_project_by_id(project_id):
    return project_service.get_project_by_id(project_id)


def update_project_by_id(project_id):
    name, cost = request.form.values()

    return project_service.update_project_by_id(project_id, name, cost)


def delete_project_by_id(project_id):
    return project_service.delete_project_by_id(project_id)


def get_company_id_by_project_id(project_id):
    project = project_service.get_project_by_id(project_id)
    return project.get('company_id')


def get_company_by_project_id(project_id):
    company_id = get_company_id_by_project_id(project_id)

    return company_service.get_company_by_id(company_id)


def get_sub_projects_by_parent_project_id(project_id):
    return project_service.get_sub_projects(project_id)


def get_parent_project_by_sub_project_id(project_id):
    project = project_service.get_project_by_id(project_id)
    parent_project_id = project.get('parent_project_id')

    return project_service.get_project_by_id(parent_project_id)


def get_employees_by_project_id(project_id):
    project_relations = project_service.get_employees_by_project_id(project_id)
    return jsonify([employee_service.get_employee_by_id(relation.get('employee_id')) for relation in project_relations])
