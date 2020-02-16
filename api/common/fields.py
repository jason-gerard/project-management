from flask_restful import fields

company_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

project_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'cost': fields.String,
    'company_id': fields.Integer,
    'parent_project_id': fields.Integer,
}
