from flask import request, Blueprint
from common.route_auth_wrappers import session_required, employee_owned_by_id, employee_and_project_owned_by_id
import controllers.employee_controller as employee_controller

employee_routes = Blueprint('employee_routes', __name__)


@employee_routes.route('', methods=['POST'])
@session_required
def company(session_company_id):
    if request.method == 'POST':
        return employee_controller.create_employee(session_company_id)


@employee_routes.route('/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
@employee_owned_by_id
def company_by_id(employee_id):
    if request.method == 'GET':
        return employee_controller.get_employee_by_id(employee_id)

    if request.method == 'PUT':
        return employee_controller.update_employee_by_id(employee_id)

    if request.method == 'DELETE':
        return employee_controller.delete_employee_by_id(employee_id)


@employee_routes.route('/<employee_id>/addToProject/<project_id>', methods=['POST'])
@employee_and_project_owned_by_id
def add_employee_to_project(employee_id, project_id):
    if request.method == 'POST':
        return employee_controller.add_employee_to_project(employee_id, project_id)


@employee_routes.route('/<employee_id>/getProjects', methods=['GET'])
@employee_owned_by_id
def get_projects_by_employee_id(employee_id):
    if request.method == 'GET':
        return employee_controller.get_projects_by_employee_id(employee_id)
