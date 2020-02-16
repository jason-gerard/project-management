from flask import Flask, g
from flask_restful import Api
from resources.projects import Projects
from resources.project import Project

app = Flask(__name__)
api = Api(app)

api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<project_id>')


@app.teardown_appcontext
def close_conn(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
