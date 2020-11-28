from flask_login import login_required, logout_user
from flask_restx import Namespace, Resource

api = Namespace('logout', description='Logout related operations')


@api.route('/')
class Logout(Resource):
    @login_required
    def post(self):
        logout_user()
