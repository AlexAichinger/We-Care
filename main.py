import logging

from flask import Flask, render_template, request, jsonify
from rauth import OAuth2Service
import os
from fb import getFriends

app = Flask(__name__)
access_token = ""

@app.route('/')
def home():
    return render_template('index.html', user='None')

@app.route('/redirect')
def redirect():
    return render_template('index.html', user='None');

@app.route('/authenticate-facebook', methods=["GET"])
def authenticate_facebook():
    FB_CLIENT_ID = '769684356512385'
    FB_CLIENT_SECRET = 'bfafc3ab14067170a74e3977643584f6'

    graph_url = 'https://graph.facebook.com/'
    facebook = OAuth2Service(
        client_id='440483442642551',
        client_secret='cd54f1ace848fa2a7ac89a31ed9c1b61',
        name='facebook',
        authorize_url='https://graph.facebook.com/oauth/authorize',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        base_url='https://graph.facebook.com/')
    redirect_uri = 'localhost:5000/redirect'
    params = {'scope': 'read_stream',
    'response_type': 'code',
    'redirect_uri': redirect_uri}
    url = facebook.get_authorize_url(**params)
    return jsonify(success=True, url=url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)