from datetime import datetime

from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('student', description='Student related operations')

# 학생조회
student_get_parser = reqparse.RequestParser()
student_get_parser.add_argument('student', type=str)
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
