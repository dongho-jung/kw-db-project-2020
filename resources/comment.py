from datetime import datetime

from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('comment', description='Comment related operations')

comment_post_parser = reqparse.RequestParser()
comment_post_parser.add_argument('post', type=str, required=True, location='form')
comment_post_parser.add_argument('content', type=str, required=True, location='form')

comment_get_parser = reqparse.RequestParser()
comment_get_parser.add_argument('post', type=str, required=True, location='form')

comment_put_parser = reqparse.RequestParser()
comment_put_parser.add_argument('comment_id', type=str, required=True)
comment_put_parser.add_argument('content', type=str)

comment_delete_parser = reqparse.RequestParser()
comment_delete_parser.add_argument('comment_id', type=str, required=True)

comment_like_or_hate_put_parser = reqparse.RequestParser()
comment_like_or_hate_put_parser.add_argument('comment_id', type=int, required=True)


@api.route('')
class Comment(Resource):
    @api.expect(comment_post_parser)
    @login_required
    def post(self):
        params = comment_post_parser.parse_args()

        post, content = params.values()
        try:
            success = db.fetch(f"SELECT * FROM class WHERE id = '{params['post']}'")[0]
        except ValueError:
            return '존재하지 않는 class_id 입니다.', 404

        author = current_user.id
        created_time = datetime.now()

        db.execute(f'''
            INSERT INTO comment(id, comment_id, post_id, content, like_, hate_, author, created_time)
            VALUES (DEFAULT, DEFAULT, {post}, '{content}', {0}, {0}, '{author}', '{created_time}')
        ''')

    @api.expect(comment_get_parser)
    def get(self):
        params = comment_get_parser.parse_args()

        predicates = []
        if params['post']: predicates += [f"post_id LIKE '%{params['post']}%'"]

        res = db.fetch(f'''
            SELECT *
            FROM comment
            WHERE {db.join_params_for_where(predicates)}
        ''')

        return res

    @api.expect(comment_put_parser)
    @login_required
    def put(self):
        params = comment_put_parser.parse_args()

        author = current_user.id
        comment_id, content = params.values()

        expected_comment_id = db.fetch(f"SELECT comment_id FROM post WHERE author = '{author}'")[0]

        if comment_id != expected_comment_id:
            return '게시글 갱신은 본인만 가능합니다.', 403

        db.execute(f'''
            UPDATE comment
            SET (content) = ('{content}')
            WHERE id = '{comment_id}'
        ''')

    @api.expect(comment_delete_parser)
    @login_required
    def delete(self):
        params = comment_delete_parser.parse_args()

        author = current_user.id
        comment_id = params['comment_id']

        expected_comment_id = db.fetch(f"SELECT comment_id FROM comment WHERE author = '{author}'")[0]

        if comment_id != expected_comment_id:
            return '게시글 삭제는 본인만 가능합니다.', 403

        db.execute(f'''
            DELETE FROM comment
            WHERE comment_id = '{comment_id}'
        ''')

    @api.route('/like')
    class CommentLike(Resource):
        @api.expect(comment_like_or_hate_put_parser)
        @login_required
        def put(self):
            params = comment_like_or_hate_put_parser.parse_args()
            comment_id = params['comment_id']

            db.execute(f'''
                UPDATE comment
                SET like_ = like_+1
                WHERE comment_id = {comment_id}
            ''')

            return

    @api.route('/hate')
    class CommentHate(Resource):
        @api.expect(comment_like_or_hate_put_parser)
        @login_required
        def put(self):
            params = comment_like_or_hate_put_parser.parse_args()
            comment_id = params['comment_id']

            db.execute(f'''
                UPDATE comment
                SET hate = hate+1
                WHERE comment_id = {comment_id}
            ''')

            return
