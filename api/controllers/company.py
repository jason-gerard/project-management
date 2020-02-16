from flask_restful import Resource, marshal_with
from common.fields import company_fields, project_fields
import services.company_service as company_service


class Company(Resource):
    def post(self):
        return company_service.create_company()


class CompanyById(Resource):
    @marshal_with(company_fields)
    def get(self, company_id):
        return company_service.get_company_by_id(company_id)

    def put(self, company_id):
        return company_service.update_company_by_id(company_id)

    def delete(self, company_id):
        return company_service.delete_company_by_id(company_id)


class GetAllProjectsByCompanyId(Resource):
    @marshal_with(project_fields)
    def get(self, company_id):
        return company_service.get_all_projects_by_company_id(company_id)
