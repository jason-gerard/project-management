from flask_restful import Resource, reqparse
from common.db_connect import make_conn
import psycopg2.extras


class Projects(Resource):
    def get(self):
        conn = make_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute('''
                    SELECT *
                    FROM projects
                    ''')
        projects = cur.fetchall()

        cur.close()

        return projects

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('cost')

        args = parser.parse_args()

        name, cost = args.values()

        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    INSERT
                    INTO projects (name, cost)
                    VALUES ('{name}', {cost})
                    ''')

        conn.commit()
        cur.close()

        return '', 201
