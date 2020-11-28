from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('student', description='Student related operations')

# 학생 조회
student_get_parser = reqparse.RequestParser()
student_get_parser.add_argument('student_id', type=str)
student_get_parser.add_argument('name', type=str)
student_get_parser.add_argument('phone', type=str)
student_get_parser.add_argument('email', type=str)

# 학생갱신
student_put_parser = reqparse.RequestParser()
student_put_parser.add_argument('name', type=str)
student_put_parser.add_argument('major_id', type=str)
student_put_parser.add_argument('year', type=int)
student_put_parser.add_argument('semester', type=int)
student_put_parser.add_argument('phone', type=str)
student_put_parser.add_argument('email', type=str)
student_put_parser.add_argument('process_id', type=str)


@api.route('')
class Student(Resource):
    @api.expect(student_get_parser)
    @login_required
    def get(self):
        params = student_get_parser.parse_args()

        predicates = []
        if params['student_id']: predicates += [f"student_id = '%{params['student_id']}%'"]
        if params['name']: predicates += [f"name LIKE '%{params['name']}%'"]
        if params['phone']: predicates += [f"phone = '%{params['phone']}%'"]
        if params['email']: predicates += [f"email = '%{params['email']}%'"]

        rows = db.fetch(f'''SELECT id, name, major_id, year, semester, phone, email, professor_id
                            FROM student
                            WHERE {db.join_params_for_where(predicates)}
               ''')
        cols = ['id', 'name', 'major_id', 'year', 'semester', 'phone', 'email', 'professor_id']

        return [{k: v for k, v in zip(cols, row)} for row in rows]

    @api.expect(student_put_parser)
    @login_required
    def put(self):
        params = student_put_parser.parse_args()
        student_id = current_user.id

        name, major_id, year, semester, phone, email, professor_id = params.values()
        db.execute(f'''
            UPDATE student_id
            SET (name, major_id, year, semester, phone, email, professor_id) = ('{name}', '{major_id}', '{year}', '{semester}', '{phone}', '{email}', '{professor_id}')
            WHERE student_id = '{student_id}'
        ''')
