import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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

conn = psycopg2.connect(
    host='localhost',
    dbname='project_management',
    user='postgres',
    password='postgres'
)

cur = conn.cursor()

create_project_table = '''
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL
)
'''

cur.execute(create_project_table)
cur.close()

conn.commit()
conn.close()
