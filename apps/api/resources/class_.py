from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('class', description='Class related operations')

class_get_parser = reqparse.RequestParser()
class_get_parser.add_argument('class_id', type=str)
class_get_parser.add_argument('year', type=int)
class_get_parser.add_argument('quarter', type=int)
class_get_parser.add_argument('class_name', type=str)
class_get_parser.add_argument('professor_id', type=str)


@api.route('')
class Class_(Resource):
    @api.expect(class_get_parser)
    def get(self):
        params = class_get_parser.parse_args()

        predicates = []
        if params['class_id']: predicates += [f"class_id = '{params['class_id']}'"]
        if params['year']: predicates += [f"year = {params['year']}"]
        if params['quarter']: predicates += [f"quarter = {params['quarter']}"]
        if params['class_name']: predicates += [f"class.name = '{params['class_name']}'"]
        if params['professor_id']: predicates += [f"professor.id = '{params['professor_id']}'"]

        rows = db.fetch(f'''
            SELECT class.name class_name, class.id class_id, professor.id professor_id, period, place, credit,
                   class.year year_, class.quarter quarter
            FROM class JOIN professor ON class.professor_id = professor.id
            WHERE {db.join_params_for_where(predicates)}
        ''')

        return [{k: v for k, v in
                 zip(['class_name', 'class_id', 'professor_id', 'period', 'place', 'credit', 'year', 'quarter'], row)}
                for
                row in rows]
