from flask_restx import Namespace, Resource

import db

api = Namespace('prereq', description='prerequisite-class related operations')


@api.route('')
class PrerequisiteClass(Resource):
    def get(self):
        return db.fetch(f'''
            SELECT *
            FROM prerequisite_class
            ORDER BY pre_class_id, class_id
        ''')
