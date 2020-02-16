from flask_restful import Resource, marshal_with
from common.fields import company_fields, project_fields
import services.project_service as project_service
import services.company_service as company_service


class Project(Resource):
    @marshal_with(project_fields)
    def get(self):
        return project_service.get_all_projects()

    def post(self):
        return project_service.create_project()


class ProjectById(Resource):
    @marshal_with(project_fields)
    def get(self, project_id):
        return project_service.get_project_by_id(project_id)

    def put(self, project_id):
        return project_service.update_project_by_id(project_id)

    def delete(self, project_id):
        return project_service.delete_project_by_id(project_id)


class GetCompanyByProjectId(Resource):
    @marshal_with(company_fields)
    def get(self, project_id):
        project = project_service.get_project_by_id(project_id)
        company_id = project['company_id']

        return company_service.get_company_by_id(company_id)


class GetSubProjectsByParentProjectId(Resource):
    @marshal_with(project_fields)
    def get(self, project_id):
        return project_service.get_sub_projects(project_id)


class GetParentProjectBySubProjectId(Resource):
    @marshal_with(project_fields)
    def get(self, project_id):
        project = project_service.get_project_by_id(project_id)
        parent_project_id = project['parent_project_id']

        return project_service.get_project_by_id(parent_project_id)
