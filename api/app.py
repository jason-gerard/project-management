from flask import Flask, g
from flask_restful import Api

from resources.project import Project, ProjectWithId, GetCompanyByProjectId
from resources.company import Company, CompanyWithId

app = Flask(__name__)
api = Api(app)

api.add_resource(Project, '/project')
api.add_resource(ProjectWithId, '/project/<project_id>')
api.add_resource(GetCompanyByProjectId, '/project/<project_id>/getCompany')

api.add_resource(Company, '/company')
api.add_resource(CompanyWithId, '/company/<company_id>')


@app.teardown_appcontext
def close_conn(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
