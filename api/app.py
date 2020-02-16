from flask import Flask, g
from flask_restful import Api

import controllers.project as project_controller
import controllers.company as company_controller

app = Flask(__name__)
api = Api(app)

api.add_resource(project_controller.Project, '/project')
api.add_resource(project_controller.ProjectById, '/project/<project_id>')
api.add_resource(project_controller.GetCompanyByProjectId, '/project/<project_id>/getCompany')
api.add_resource(project_controller.GetSubProjectsByParentProjectId, '/project/<project_id>/getSubProjects')
api.add_resource(project_controller.GetParentProjectBySubProjectId, '/project/<project_id>/getParentProject')

api.add_resource(company_controller.Company, '/company')
api.add_resource(company_controller.CompanyById, '/company/<company_id>')
api.add_resource(company_controller.GetAllProjectsByCompanyId, '/company/<company_id>/getProjects')


@app.teardown_appcontext
def close_conn(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
