from flask_restful import Resource, reqparse
from common.db_connect import make_conn
import psycopg2.extras


class Project(Resource):
    def get(self):
        conn = make_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute('''
                    SELECT *
                    FROM project
                    ''')
        projects = cur.fetchall()

        cur.close()

        return projects

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('cost')
        parser.add_argument('company_id')

        args = parser.parse_args()

        name, cost, company_id = args.values()

        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    INSERT
                    INTO project (name, cost, company_id)
                    VALUES ('{name}', {cost}, {company_id})
                    ''')

        conn.commit()
        cur.close()

        return '', 201


class ProjectWithId(Resource):
    def get(self, project_id):
        conn = make_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute(f'''
                    SELECT *
                    FROM project
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
                    UPDATE project
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
                    FROM project
                    WHERE id = {project_id}
                    ''')

        conn.commit()
        cur.close()

        return '', 204


class GetCompanyByProjectId(Resource):
    def get(self, projectId):
        pass
