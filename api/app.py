from flask import Flask, g
from config import secret_key
from routes.project_routes import project_routes
from routes.company_routes import company_routes
from routes.auth_routes import auth_routes

app = Flask(__name__)

app.register_blueprint(project_routes, url_prefix='/project')
app.register_blueprint(company_routes, url_prefix='/company')
app.register_blueprint(auth_routes, url_prefix='/auth')

app.secret_key = secret_key


@app.teardown_appcontext
def close_conn(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
