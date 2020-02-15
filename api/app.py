from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

projects = [
    {
        'name': 'project1',
        'cost': 50000
    },
    {
        'name': 'project2',
        'cost': 10000
    }
]

parser = reqparse.RequestParser()
parser.add_argument('cost')


class Project(Resource):
    def get(self, project_id):
        return projects[int(project_id) - 1]

    def put(self, project_id):
        args = parser.parse_args()
        projects[int(project_id) - 1]['cost'] = int(args['cost'])
        return projects[int(project_id) - 1], 201

    def delete(self, project_id):
        del projects[int(project_id) - 1]
        return f'Project of id {project_id} was deleted', 204


class Projects(Resource):
    def get(self):
        return projects

    def post(self):
        args = parser.parse_args()
        index = len(projects) + 1

        projects.append({
            'name': f'project{index}',
            'cost': int(args['cost'])
        })

        return projects, 201


api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<project_id>')

if __name__ == '__main__':
    app.run(debug=True)
