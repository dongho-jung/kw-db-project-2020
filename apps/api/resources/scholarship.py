import pandas as pd
from flask_login import login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('scholarship', description='Scholarship related operations')

scholarship_get_parser = reqparse.RequestParser()
scholarship_get_parser.add_argument('start_year', type=str)


@api.route('/')
class Scholarship(Resource):
    @api.expect(scholarship_get_parser)
    @login_required
    def get(self):
        params = scholarship_get_parser.parse_args()

        start_year = params['start_year']

        rows = db.fetch(f'''
            WITH avg_grade_tab AS (
                SELECT year, AVG(grade) avg_grade
                FROM grade
                WHERE year >= {start_year}
                GROUP BY year, student_id
            ),
            unique_grade_tab AS (
                SELECT DISTINCT year, avg_grade
                FROM avg_grade_tab
            ),
            rank_grade_tab AS (
                SELECT *,
                    DENSE_RANK() OVER (PARTITION BY year ORDER BY avg_grade DESC) rank_
                FROM unique_grade_tab
            )
            SELECT year, rank_, ROUND(avg_grade, 3)::FLOAT
            FROM rank_grade_tab
            WHERE rank_ IN (1,2,10)
            ORDER BY year
        ''')

        result = [tuple(r) for r in pd.DataFrame(rows, columns=['year', 'rank', 'threshold'])
            .astype({'year': int, 'threshold': float})
            .pivot(index='year', columns='rank', values='threshold')
            .values]

        return result
