from flask_restful import Resource, reqparse
from common.db_connect import make_conn
import psycopg2.extras


class Project(Resource):
    def get(self, project_id):
        conn = make_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute(f'''
                    SELECT *
                    FROM projects
                    WHERE id = {project_id}
                    ''')

        project = cur.fetchone()

        cur.close()

        return project

    def put(self, project_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('cost')

        args = parser.parse_args()

        name, cost = args.values()

        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    UPDATE projects
                    SET name = '{name}',
                        cost = {cost}
                    WHERE id = {project_id}
                    ''')

        conn.commit()
        cur.close()

        return '', 201

    def delete(self, project_id):
        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    DELETE
                    FROM projects
                    WHERE id = {project_id}
                    ''')

        conn.commit()
        cur.close()

        return '', 204
