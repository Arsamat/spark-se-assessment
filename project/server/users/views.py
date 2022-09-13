from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class GetUsersAPI(MethodView):

    def get(self):
        result = {}
        result["users"] = []
        users = User.query.all()
        for user in users:
            temp = {"admin": user.admin, "email": user.email, "id": user.id, "registered_on": user.registered_on
            }
            result["users"].append(temp)

        return result


# define the API resources
users_view = GetUsersAPI.as_view('getusers_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)