import psycopg2
from flask import g
from config import DBConnection


def make_conn():
    return psycopg2.connect(
        host=DBConnection.host.value,
        dbname=DBConnection.dbname.value,
        user=DBConnection.user.value,
        password=DBConnection.password.value
    )


def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._databse = make_conn()
    return conn
