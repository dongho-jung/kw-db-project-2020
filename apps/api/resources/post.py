from datetime import datetime

from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('post', description='Post related operations')

post_post_parser = reqparse.RequestParser()
post_post_parser.add_argument('title', type=str, required=True, location='form')
post_post_parser.add_argument('content', type=str, required=True, location='form')
post_post_parser.add_argument('is_notice', type=bool, required=True, location='form')
post_post_parser.add_argument('class_id', type=str, required=True, location='form')

post_get_parser = reqparse.RequestParser()
post_get_parser.add_argument('title', type=str)
post_get_parser.add_argument('content', type=str)
post_get_parser.add_argument('is_notice', type=bool)
post_get_parser.add_argument('class_id', type=str)
post_get_parser.add_argument('year', type=int)
post_get_parser.add_argument('quarter', type=int)

post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument('post_id', type=str, required=True)
post_put_parser.add_argument('title', type=str)
post_put_parser.add_argument('content', type=str)

post_delete_parser = reqparse.RequestParser()
post_delete_parser.add_argument('post_id', type=str, required=True)


@api.route('/')
class Post(Resource):
    @api.expect(post_post_parser)
    @login_required
    def post(self):
        params = post_post_parser.parse_args()

        title, content, is_notice, class_id = params.values()
        try:
            year, quarter = db.fetch(f"SELECT year, quarter FROM class WHERE id = '{params['class_id']}'")[0]
        except ValueError:
            return '존재하지 않는 class_id 입니다.', 404

        author = current_user.id
        created_time = datetime.now()

        db.execute(f'''
            INSERT INTO post(id, title, content, is_notice, class_id, year, quarter, author, created_time)
            VALUES (DEFAULT, '{title}', '{content}', {is_notice}, '{class_id}', {year}, {quarter}, '{author}', '{created_time}')
        ''')

    @api.expect(post_get_parser)
    def get(self):
        params = post_get_parser.parse_args()

        predicates = []
        if params['title']: predicates += [f"title LIKE '%{params['title']}%'"]
        if params['content']: predicates += [f"content LIKE '%{params['content']}%'"]
        if params['is_notice']: predicates += [f"is_notice = {params['is_notice']}"]
        if params['class_id']: predicates += [f"class_id = '{params['class_id']}'"]
        if params['year']: predicates += [f"year = {params['year']}"]
        if params['quarter']: predicates += [f"quarter = {params['quarter']}"]

        res = db.fetch(f'''
            SELECT id
            FROM post
            WHERE {db.join_params_for_where(predicates)}
        ''')

        return res

    @api.expect(post_put_parser)
    @login_required
    def put(self):
        params = post_put_parser.parse_args()

        post_id, title, content = params.values()
        
        expected_post_id = db.fetch(f"SELECT post_id FROM post WHERE author = '{current_user.id}'")[0]

        if post_id != expected_post_id:
            return '게시글 갱신은 본인만 가능합니다.', 403

        db.execute(f'''
            UPDATE post
            SET (title, content) = ('{title}', '{content}')
            WHERE id = '{post_id}'
        ''')

    @api.expect(post_delete_parser)
    @login_required
    def delete(self):
        params = post_delete_parser.parse_args()

        post_id = params['post_id']

        expected_post_id = db.fetch(f"SELECT post_id FROM post WHERE author = '{current_user.id}'")[0]

        if post_id != expected_post_id:
            return '게시글 삭제는 본인만 가능합니다.', 403

        db.execute(f'''
            DELETE FROM post
            WHERE id = '{post_id}'
        ''')
