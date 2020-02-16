from flask import request, Blueprint
from common.route_auth_wrappers import session_required, company_owned_by_id
import controllers.company_controller as company_controller

company_routes = Blueprint('company_routes', __name__)


@company_routes.route('', methods=['GET', 'POST'])
def company():
    if request.method == 'POST':
        return company_controller.create_company()


@company_routes.route('/<company_id>', methods=['GET', 'PUT', 'DELETE'])
@company_owned_by_id
def company_by_id(company_id):
    if request.method == 'GET':
        return company_controller.get_company_by_id(company_id)

    if request.method == 'PUT':
        return company_controller.update_company_by_id(company_id)

    if request.method == 'DELETE':
        return company_controller.delete_company_by_id(company_id)


@company_routes.route('/<company_id>/getProjects', methods=['GET'])
@company_owned_by_id
def get_all_projects_by_company_id(company_id):
    if request.method == 'GET':
        return company_controller.get_all_projects_by_company_id(company_id)


@company_routes.route('/my_company', methods=['GET'])
@session_required
def my_company(session_company_id):
    if request.method == 'GET':
        return company_controller.get_company_by_id(session_company_id)
