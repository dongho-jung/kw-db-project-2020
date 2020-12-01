from datetime import datetime

from flask_login import current_user, login_required
from flask_restx import Namespace, Resource, reqparse

import db

api = Namespace('comment', description='Comment related operations')

comment_post_parser = reqparse.RequestParser()
comment_post_parser.add_argument('post_id', type=str, location='form')
comment_post_parser.add_argument('comment_id', type=str, location='form')
comment_post_parser.add_argument('content', type=str, required=True, location='form')

comment_get_parser = reqparse.RequestParser()
comment_get_parser.add_argument('post_id', type=str, required=True)

comment_put_parser = reqparse.RequestParser()
comment_put_parser.add_argument('comment_id', type=str, required=True, location='form')
comment_put_parser.add_argument('content', type=str, required=True, location='form')

comment_delete_parser = reqparse.RequestParser()
comment_delete_parser.add_argument('comment_id', type=str, required=True, location='form')

comment_like_or_hate_put_parser = reqparse.RequestParser()
comment_like_or_hate_put_parser.add_argument('comment_id', type=int, required=True, location='form')


@api.route('')
class Comment(Resource):
    @api.expect(comment_post_parser)
    @login_required
    def post(self):
        params = comment_post_parser.parse_args()

        author = current_user.id
        content = params['content']
        created_time = datetime.now()

        db.execute(f'''
            INSERT INTO comment(id, comment_id, post_id, content, like_, hate, author, created_time)
            VALUES (DEFAULT, {params['comment_id'] or 'DEFAULT'}, {params['post_id'] or 'DEFAULT'}, '{content}',
                    DEFAULT, DEFAULT, '{author}', '{created_time}')
        ''')

    @api.expect(comment_get_parser)
    def get(self):
        params = comment_get_parser.parse_args()

        rows = db.fetch(f'''
            SELECT id, comment_id, post_id, content, like_, hate, author, created_time::TEXT
            FROM comment
            WHERE post_id = {params['post_id']}
        ''')
        cols = ['id', 'comment_id', 'post_id', 'content', 'like_', 'hate', 'author', 'created_time']
        return [{k: v for k, v in zip(cols, row)} for row in rows]

    @api.expect(comment_put_parser)
    @login_required
    def put(self):
        params = comment_put_parser.parse_args()

        author = current_user.id
        comment_id, content = params.values()

        if not db.fetch(f"SELECT * FROM comment WHERE author = '{author}' AND id = '{comment_id}'"):
            return '댓글 갱신은 본인만 가능합니다.', 403

        db.execute(f'''
            UPDATE comment
            SET content = '{content}'
            WHERE id = '{comment_id}'
        ''')

    @api.expect(comment_delete_parser)
    @login_required
    def delete(self):
        params = comment_delete_parser.parse_args()

        author = current_user.id
        comment_id = params['comment_id']

        if not db.fetch(f"SELECT * FROM comment WHERE author = '{author}' AND id = '{comment_id}'"):
            return '댓글 삭제는 본인만 가능합니다.', 403

        db.execute(f'''
            DELETE FROM comment
            WHERE id = '{comment_id}'
        ''')


@api.route('/like')
class CommentLike(Resource):
    @api.expect(comment_like_or_hate_put_parser)
    @login_required
    def put(self):
        params = comment_like_or_hate_put_parser.parse_args()

        student_id = current_user.id
        comment_id = params['comment_id']

        if db.fetch(
                f"SELECT * FROM comment_vote WHERE student_id='{student_id}' AND post_id={comment_id} AND like_or_hate=TRUE"):
            return "이미 좋아요를 하셨습니다.", 400

        db.execute(f'''
            INSERT INTO comment_vote
            VALUES ('{student_id}', {comment_id}, TRUE)
        ''')

        db.execute(f'''
            UPDATE comment
            SET like_ = like_+1
            WHERE comment_id = {comment_id}
        ''')


@api.route('/hate')
class CommentHate(Resource):
    @api.expect(comment_like_or_hate_put_parser)
    @login_required
    def put(self):
        params = comment_like_or_hate_put_parser.parse_args()

        student_id = current_user.id
        comment_id = params['comment_id']

        if db.fetch(
                f"SELECT * FROM comment_vote WHERE student_id='{student_id}' AND post_id={comment_id} AND like_or_hate=FALSE"):
            return "이미 싫어요 하셨습니다.", 400

        db.execute(f'''
            INSERT INTO comment_vote
            VALUES ('{student_id}', {comment_id}, FALSE)
        ''')

        db.execute(f'''
            UPDATE comment
            SET hate = hate+1
            WHERE comment_id = {comment_id}
        ''')
