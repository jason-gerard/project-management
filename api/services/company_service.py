from flask import jsonify
from common.db_connect import make_conn
import psycopg2.extras


def create_company(user):
    conn = make_conn()
    cur = conn.cursor()

    cur.execute(f'''
                INSERT
                INTO company (name, username, password)
                VALUES ('{user['name']}', '{user['username']}', '{user['password']}')
                ''')

    conn.commit()
    cur.close()

    return '', 201


def get_company_by_id(company_id):
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


def update_company_by_id(company_id, name):
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


def delete_company_by_id(company_id):
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


def get_all_projects_by_company_id(company_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM project
                WHERE company_id = {company_id}
                ''')

    projects = cur.fetchall()

    cur.close()

    return jsonify(projects)


def get_company_by_username(username):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM company
                WHERE username = '{username}'
                ''')

    company = cur.fetchone()

    cur.close()

    return company


def get_employees_by_company_id(company_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM employee
                WHERE company_id = {company_id}
                ''')

    projects = cur.fetchall()

    cur.close()

    return jsonify(projects)
