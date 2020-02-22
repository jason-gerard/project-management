from flask import jsonify
from common.db_connect import make_conn
import psycopg2.extras


def create_project(name, cost, company_id, parent_project_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                INSERT
                INTO project (name, cost, company_id, parent_project_id)
                VALUES ('{name}', {cost}, {company_id}, {parent_project_id})
                RETURNING id
                ''')

    project_id = cur.fetchone()

    conn.commit()
    cur.close()

    return project_id, 201


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


def update_project_by_id(project_id, name, cost):
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

    return jsonify(projects)


def get_employees_by_project_id(project_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM employee_project
                WHERE project_id = {project_id}
                ''')

    projects = cur.fetchall()

    cur.close()

    return projects
