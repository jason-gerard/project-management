from flask import request, Blueprint, session
import controllers.company_controller as company_controller

company_routes = Blueprint('company_routes', __name__)


@company_routes.route('', methods=['GET', 'POST'])
def company():
    if request.method == 'POST':
        return company_controller.create_company()


@company_routes.route('/<company_id>', methods=['GET', 'PUT', 'DELETE'])
def company_by_id(company_id):
    if request.method == 'GET':
        return company_controller.get_company_by_id(company_id)

    if request.method == 'PUT':
        return company_controller.update_company_by_id(company_id)

    if request.method == 'DELETE':
        return company_controller.delete_company_by_id(company_id)


@company_routes.route('/<company_id>/getProjects', methods=['GET'])
def get_all_projects_by_company_id(company_id):
    if request.method == 'GET':
        return company_controller.get_all_projects_by_company_id(company_id)


@company_routes.route('/my_company', methods=['GET'])
def my_company():
    company_id = session['company_id']

    if request.method == 'GET':
        return company_controller.get_company_by_id(company_id)
