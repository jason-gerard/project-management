import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='project_management',
    user='postgres',
    password='postgres'
)
