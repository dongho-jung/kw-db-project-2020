from flask_login import login_required, current_user
from flask_restx import Namespace, Resource, reqparse

import db
import util

api = Namespace('enroll', description='Enroll related operations')

enroll_post_parser = reqparse.RequestParser()
enroll_post_parser.add_argument('class_ids', required=True, location='form', action='split')


@api.route('')
class Enroll(Resource):
    @api.expect(enroll_post_parser)
    @login_required
    def post(self):
        params = enroll_post_parser.parse_args()

        class_ids = params['class_ids']
        student_id = current_user.id

        year, quarter = util.get_year_and_quarter()

        for class_id in class_ids:
            db.execute(f'''
                INSERT INTO grade
                VALUES ('{student_id}', '{class_id}', {year}, {quarter}, NULL, NULL)
            ''')
