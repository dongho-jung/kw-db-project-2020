from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('student', description='Student related operations')

# 학생갱신
student_put_parser = reqparse.RequestParser()
student_put_parser.add_argument('name', type=str)
student_put_parser.add_argument('major_id', type=str)
student_put_parser.add_argument('year', type=int)
student_put_parser.add_argument('semester', type=int)
student_put_parser.add_argument('phone', type=str)
student_put_parser.add_argument('email', type=str)
student_put_parser.add_argument('process_id', type=str)

student_check_email_parser = reqparse.RequestParser()
student_check_email_parser.add_argument('email', required=True, type=str)


@api.route('')
class Student(Resource):
    @login_required
    def get(self):
        student_id = current_user.id

        rows = db.fetch(f'''SELECT id, name, major_id, year, semester, phone, email, professor_id
                            FROM student
                            WHERE id = {student_id}
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


@api.route('/check/email')
class StudentCheckEmail(Resource):
    @api.expect(student_check_email_parser)
    def get(self):
        params = student_put_parser.parse_args()
        email = params['email']

        rows = db.fetch(f'''SELECT 1
                            FROM student
                            WHERE email = '{email}'
               ''')

        if rows:
            return {'msg': '이미 존재하는 이메일입니다.'}, 409
        else:
            return 200
