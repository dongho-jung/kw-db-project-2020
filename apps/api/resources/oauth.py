from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_login import login_required, current_user
from flask_restx import Namespace, Resource
import requests
import json
from urllib.parse import urlunsplit, urlencode
from collections import OrderedDict

import db
import util

api = Namespace('oauth', description='Login related kakao_api')

CLIENT_ID = '8d323fc0c13720cda59983912f875316'
REDIRECT_URL = 'http://localhost:5000/oauth'
GET_KAKAO_AUTHENTICATION_CODE = 'https://kauth.kakao.com/oauth/authorize?client_id=' + CLIENT_ID + \
                                '&redirect_uri=' + REDIRECT_URL + '&response_type=code'

@api.route('')
class Ouath(Resource):
    def get(self):
        code = str(request.args.get('code'))
        CLIENT_ID = '8d323fc0c13720cda59983912f875316'
        REDIRECT_URL = 'http://localhost:5000/oauth'
        print('user_code: ' + code)
        url = "https://kauth.kakao.com/oauth/token"
        payload = {"grant_type": "authorization_code", "client_id": CLIENT_ID, "redirect_uri": REDIRECT_URL,
                   "code": code}
        print(payload)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload)
        access_token = json.loads(((response.text).encode('utf-8')))['access_token']
        print("access token: " + access_token)

        url = "https://kapi.kakao.com/v1/user/signup"
        headers.update({'Authorization': "Bearer " + access_token})
        response = requests.request("POST", url, headers=headers)
        print("signup response: " + response.text)

        url = "https://kapi.kakao.com/v2/user/me"
        response = requests.request("POST", url, headers=headers)
        print("me response: " + response.text)
        resp = json.loads(json.dumps(response.text, ensure_ascii=False))
        resp_list = list(map(str, resp.split('"')))

        resp_list_p = list()
        for i in range(len(resp_list)):
            if len(resp_list[i]) > 2:
                resp_list_p.append(resp_list[i])
        resp_list = resp_list_p

        unique_id = resp_list[0].replace(" : ", "").replace(" ' ", "").replace(" , ", "")
        nickname = resp_list[resp_list.index('nickname') + 1].replace(" ' ", "")
        email = resp_list[resp_list.index('email') + 1].replace(" ' ", "")
        gender = resp_list[resp_list.index('gender') + 1].replace(" ' ", "")
        birthday = resp_list[resp_list.index('birthday') + 1].replace(" ' ", "")
        profile_image = resp_list[resp_list.index('profile_image_url') + 1].replace(" ' ", "")

        query_string = urlencode(OrderedDict(**{'unique_id': unique_id, 'nickname': nickname, 'email': email, 'gender': gender, 'birthday': birthday,
                'profile_image': profile_image}))

        url = 'http://localhost:3000/login?' + query_string

        return redirect(url, code=302)
        #
        # return {'unique_id': unique_id, 'nickname': nickname, 'email': email, 'gender': gender, 'birthday': birthday,
        #         'profile_image': profile_image}
