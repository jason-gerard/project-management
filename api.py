from flask import Flask
from flask_restful import Resource, Api

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


class Project(Resource):
    def get(self, project_id):
        return projects[int(project_id) - 1]


class Projects(Resource):
    def get(self):
        return projects

    def post(self):
        index = len(projects) + 1
        projects.append({
            'name': f'project{index}',
            'cost': 100
        })

        return projects, 201


api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<project_id>')

if __name__ == '__main__':
    app.run(debug=True)
