from flask_login import login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('class', description='class related operations')

# 과목 조회
class_get_parser = reqparse.RequestParser()
class_get_parser.add_argument('class_id', type=str)
class_get_parser.add_argument('year', type=int)
class_get_parser.add_argument('quarter', type=int)
class_get_parser.add_argument('name', type=str)
class_get_parser.add_argument('class_professor', type=str)


@api.route('/')
class Class(Resource):
    # 과목 조회
    @api.expect(class_get_parser)
    @login_required
    def get(self):
        params = class_get_parser.parse_args()

        predicates = []
        if params['class_id'] : predicates += [f"class_id LIKE '%{params['class_id']}%'"]
        if params['year'] : predicates += [f"year LIKE '%{params['year']}%'"]
        if params['quarter'] : predicates += [f"quarter LIKE '%{params['quarter']}%'"]
        if params['name'] : predicates += [f"name LIKE '%{params['name']}%'"]
        if params['class_professor'] : predicates += [f"class_professor LIKE '%{params['class_professor']}%'"]

        try:
            whatyouwant_list = db.fetch(f'''SELECT * FROM post WHERE {db.join_params_for_where(predicates)}''')
            res = [{'name': whatyouwant_list[5]}, {'credit': whatyouwant_list[9]}] #추가 예정
            return res
        except ValueError:
            return False
