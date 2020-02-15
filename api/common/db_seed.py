import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from api.common.db_connect import get_conn

initialConn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres'
)

initialConn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = initialConn.cursor()

cur.execute('DROP DATABASE IF EXISTS project_management')
cur.execute('CREATE DATABASE project_management')

cur.close()
initialConn.close()

conn = get_conn()
cur = conn.cursor()

create_project_table = '''
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    cost MONEY NOT NULL
)
'''

cur.execute(create_project_table)

conn.commit()

cur.close()

conn.close()
