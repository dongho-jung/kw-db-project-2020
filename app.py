from flask import Flask
from flask_restx import Api

from resources.student import api as student_api

app = Flask(__name__)
api = Api(app, version='1.0', title='KW SIS API', description='A Student Inforamtion System API for KwangWoon univ')

api.add_namespace(student_api)

if __name__ == '__main__':
    app.run(debug=True)
