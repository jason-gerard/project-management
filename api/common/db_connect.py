import psycopg2
from flask import g


def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._databse = psycopg2.connect(
            host='localhost',
            dbname='project_management',
            user='postgres',
            password='postgres'
        )
    return conn

