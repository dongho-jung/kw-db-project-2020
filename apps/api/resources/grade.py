from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('grade', description='Grade related operations')

grade_get_parser = reqparse.RequestParser()
grade_get_parser.add_argument('year', type=str)
grade_get_parser.add_argument('quarter', type=str)
grade_get_parser.add_argument('retake', type=bool)
grade_get_parser.add_argument('grade', type=str)


@api.route('')
class Grade(Resource):
    @api.expect(grade_get_parser)
    @login_required
    def get(self):
        params = grade_get_parser.parse_args()

        student_id = current_user.id

        predicates = [f"student_id = '{student_id}'"]
        if params['year']: predicates += [f"grade.year = {params['year']}"]
        if params['quarter']: predicates += [f"grade.quarter = {params['quarter']}"]
        if params['retake']: predicates += [f"retake = {params['retake']}"]
        if params['grade']: predicates += [f"grade = {params['grade']}"]

        return db.fetch(f'''
                    SELECT name, credit, classification, grade::FLOAT, grade.year, grade.quarter
                    FROM grade JOIN class ON class.id = grade.class_id
                    WHERE {db.join_params_for_where(predicates)}
                ''')
