from flask_restful import reqparse
from common.db_connect import make_conn
import psycopg2.extras


def get_all_projects():
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute('''
                SELECT *
                FROM project
                ''')

    projects = cur.fetchall()

    cur.close()

    return projects


def create_project():
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('cost', type=int, required=True)
    parser.add_argument('company_id', required=True)
    parser.add_argument('parent_project_id')

    args = parser.parse_args()

    name, cost, company_id, parent_project_id = args.values()

    parent_project_id = 'null' if not parent_project_id else parent_project_id

    print('parent_project_id', type(parent_project_id), parent_project_id, len(parent_project_id))

    conn = make_conn()
    cur = conn.cursor()

    cur.execute(f'''
                INSERT
                INTO project (name, cost, company_id, parent_project_id)
                VALUES ('{name}', {cost}, {company_id}, {parent_project_id})
                ''')

    conn.commit()
    cur.close()

    return '', 201


def get_project_by_id(project_id):
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


def update_project_by_id(project_id):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('cost', type=int, required=True)

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


def delete_project_by_id(project_id):
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


def get_sub_projects(project_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM project
                WHERE parent_project_id = {project_id}
                ''')

    projects = cur.fetchall()

    cur.close()

    return projects
