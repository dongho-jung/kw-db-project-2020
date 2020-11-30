from flask_login import LoginManager, UserMixin

login_manager = LoginManager()


class User(UserMixin):
    def __init__(self, student_id):
        self.id = student_id

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized_handler():
    return {'msg': '로그인 먼저 해주시기 바랍니다.'}, 403
