from flask import request, Blueprint
from common.route_auth_wrappers import session_required
import controllers.auth_controller as auth_controller
import controllers.company_controller as company_controller

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signIn', methods=['POST'])
def sign_in():
    if request.method == 'POST':
        return auth_controller.sign_in()


@auth_routes.route('/signOut', methods=['GET'])
@session_required
def sign_out(company_id):
    if request.method == 'GET':
        return auth_controller.sign_out(company_id)


@auth_routes.route('/signUp', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        company_controller.create_company()
        return auth_controller.sign_in()
