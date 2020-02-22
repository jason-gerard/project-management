from common.db_connect import make_conn
import psycopg2.extras


def create_employee(company_id, name):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                INSERT
                INTO employee (name, company_id)
                VALUES ('{name}', {company_id})
                RETURNING id
                ''')

    employee_id = cur.fetchone()

    conn.commit()
    cur.close()

    return employee_id, 201


def get_employee_by_id(employee_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM employee
                WHERE id = {employee_id}
                ''')

    project = cur.fetchone()

    cur.close()

    return project


def update_employee_by_id(employee_id, name):
    conn = make_conn()
    cur = conn.cursor()

    cur.execute(f'''
                UPDATE employee
                SET name = '{name}'
                WHERE id = {employee_id}
                ''')

    conn.commit()
    cur.close()

    return '', 201


def delete_employee_by_id(employee_id):
    conn = make_conn()
    cur = conn.cursor()

    cur.execute(f'''
                DELETE
                FROM employee
                WHERE id = {employee_id}
                ''')

    conn.commit()
    cur.close()

    return '', 204


def add_employee_to_project(employee_id, project_id):
    conn = make_conn()
    cur = conn.cursor()

    cur.execute(f'''
                INSERT
                INTO employee_project (employee_id, project_id)
                VALUES ({employee_id}, {project_id})
                ''')

    conn.commit()
    cur.close()

    return '', 201


def get_projects_by_employee_id(employee_id):
    conn = make_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(f'''
                SELECT *
                FROM employee_project
                WHERE employee_id = {employee_id}
                ''')

    projects = cur.fetchall()

    cur.close()

    return projects
