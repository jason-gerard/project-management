from flask import request, session
import services.project_service as project_service
import services.company_service as company_service


def get_all_projects():
    return project_service.get_projects()


def create_project():
    name, cost, company_id, parent_project_id = request.form.values()

    return project_service.create_project(name, cost, company_id, parent_project_id)


def get_project_by_id(project_id):
    return project_service.get_project_by_id(project_id)


def update_project_by_id(project_id):
    name, cost = request.form.values()

    return project_service.update_project_by_id(project_id, name, cost)


def delete_project_by_id(project_id):
    return project_service.delete_project_by_id(project_id)


def get_company_by_project_id(project_id):
    project = project_service.get_project_by_id(project_id)
    company_id = project['company_id']

    return company_service.get_company_by_id(company_id)


def get_sub_projects_by_parent_project_id(project_id):
    return project_service.get_sub_projects(project_id)


def get_parent_project_by_sub_project_id(project_id):
    project = project_service.get_project_by_id(project_id)
    parent_project_id = project['parent_project_id']

    return project_service.get_project_by_id(parent_project_id)
