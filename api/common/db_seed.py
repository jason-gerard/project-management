import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from db_connect import make_conn

initialConn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres'
)

initialConn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = initialConn.cursor()

cur.execute('''
            DROP DATABASE IF
            EXISTS project_management
            ''')
cur.execute('''
            CREATE DATABASE project_management
            ''')

cur.close()
initialConn.close()

conn = make_conn()
cur = conn.cursor()

commands = (
    '''
    CREATE TABLE company (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    ''',
    '''
    CREATE TABLE project (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        cost MONEY NOT NULL,
        company_id SERIAL REFERENCES company (id)
    )
    '''
)

for command in commands:
    cur.execute(command)

conn.commit()

cur.close()

conn.close()
