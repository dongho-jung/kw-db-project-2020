from flask_login import login_required, current_user
from flask_restx import Namespace, Resource

import db
import util

api = Namespace('timetable', description='Timetable related operations')


@api.route('')
class Timetable(Resource):
    @login_required
    def get(self):
        student_id = current_user.id

        year, quarter = util.get_year_and_quarter()

        rows = db.fetch(f'''
            SELECT name, period
            FROM grade JOIN class ON grade.class_id = class.id
            WHERE grade.year = {year} AND grade.quarter = {quarter}
              AND class.year = {year} AND class.quarter = {quarter}
              AND student_id = '{student_id}'
        ''')

        return [{'name': name, 'period': period.split()} for name, period in rows]
