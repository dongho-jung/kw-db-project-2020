import itertools
from collections import namedtuple, defaultdict

from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('wizard', description='Wizard related operations')

wizard_get_parser = reqparse.RequestParser()
wizard_get_parser.add_argument('year', type=int, required=True)
wizard_get_parser.add_argument('quarter', type=int, required=True)
wizard_get_parser.add_argument('desired_credit', type=int, required=True)
wizard_get_parser.add_argument('prefer_time', type=str,
                               help="NULL->don't care, early->period 1~4, late->period 3~6, free_%a->no class in the weekday")
wizard_get_parser.add_argument('prefer_cap', type=str, help="NULL->don't care, small->cap <= 40, large->cap > 40")
wizard_get_parser.add_argument('offset', type=int, help='default 0')


def gen_periods(period_classes, desired_credit):
    for n in range(desired_credit // 3, desired_credit):
        for case in itertools.combinations(period_classes, n):
            if len(' '.join(case).split()) == desired_credit:
                yield case


@api.route('')
class Wizard(Resource):
    @api.expect(wizard_get_parser)
    def get(self):
        params = wizard_get_parser.parse_args()

        year, quarter, desired_credit, prefer_time, prefer_cap, offset = params.values()
        offset = offset or 0
        CHUNK_SIZE = 10

        rows = db.fetch(f'''
            SELECT class.name class_name, period, credit, capacity
            FROM class JOIN professor ON class.professor_id = professor.id
            WHERE class.year = {year} AND class.quarter = {quarter}
        ''')
        Class = namedtuple('Class', ['name', 'period', 'credit', 'capacity'])

        invalid_pred = lambda x: any(str(i) in x.period for i in (7, 8)) or any(i in x.period for i in ('SAT', 'SUN'))
        classes = [Class(*row) for row in rows]
        classes = [c for c in classes if not invalid_pred(c)]

        if prefer_time:
            if '_' not in prefer_time:
                invalid_range = {'early': range(3, 7), 'late': range(1, 5)}[prefer_time]
            else:
                invalid_range = [params['prefer_time'].split('_')[-1]]
            classes = [c for c in classes if not any(str(i) in ''.join(c.period) for i in invalid_range)]

        if prefer_cap:
            if prefer_cap == 'small':
                pred_cap = lambda x: x <= 40
            elif prefer_cap == 'large':
                pred_cap = lambda x: x > 40
            else:
                return {'msg': 'prefer_cap을 제대로 입력해주세요.'}, 400
            classes = [c for c in classes if pred_cap(c.capacity)]

        period_classes = defaultdict(list)
        for c in classes:
            period_classes[c.period] += [c]

        W = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}
        result = []
        for periods in gen_periods(period_classes, desired_credit):
            for case in itertools.product(*[period_classes[p] for p in periods]):
                tmp = [[(c.name, W[p[:-1]], int(p[-1])) for p in c.period.split()] for c in case]
                result += [list(itertools.chain.from_iterable(tmp))]
                if len(result) >= CHUNK_SIZE:
                    return result[offset:offset + CHUNK_SIZE]
