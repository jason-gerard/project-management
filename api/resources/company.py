from flask_restful import Resource, reqparse
from common.db_connect import make_conn
import psycopg2.extras


class Company(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')

        args = parser.parse_args()

        name = args['name']

        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    INSERT
                    INTO company (name)
                    VALUES ('{name}')
                    ''')

        conn.commit()
        cur.close()

        return '', 201


class CompanyWithId(Resource):
    def get(self, company_id):
        conn = make_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        cur.execute(f'''
                    SELECT *
                    FROM company
                    WHERE id = {company_id}
                    ''')

        company = cur.fetchone()

        cur.close()

        return company

    def put(self, company_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')

        args = parser.parse_args()

        name = args['name']

        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    UPDATE company
                    SET name = '{name}'
                    WHERE id = {company_id}
                    ''')

        conn.commit()
        cur.close()

        return '', 201

    def delete(self, company_id):
        conn = make_conn()
        cur = conn.cursor()

        cur.execute(f'''
                    DELETE
                    FROM company
                    WHERE id = {company_id}
                    ''')

        conn.commit()
        cur.close()

        return '', 204
