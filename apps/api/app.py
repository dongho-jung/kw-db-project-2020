import os

from flask import Flask
from flask_restx import Api

from kw_sis_session import login_manager
from resources.login import api as login_api
from resources.logout import api as logout_api
from resources.post import api as post_api
from resources.scholarship import api as scholarship_api
from resources.enroll import api as enroll_api

app = Flask(__name__)
app.secret_key = os.environ['KW_APP_SECRET']

login_manager.init_app(app)

api = Api(app, version='1.0', title='KW SIS API',
          description='A Student Information System API for KwangWoon univ'
          )

api.add_namespace(post_api)
api.add_namespace(login_api)
api.add_namespace(logout_api)
api.add_namespace(scholarship_api)
api.add_namespace(enroll_api)

if __name__ == '__main__':
    app.run(debug=True)
