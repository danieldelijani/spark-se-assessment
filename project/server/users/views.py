from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class UsersApi(MethodView):

    def get(self):
        all_users = [entry.email for entry in User.query.all()]
        return str(all_users)

# define the API resources
users_view = UsersApi.as_view('register_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)