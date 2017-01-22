from flask import Flask, render_template, request, jsonify
#from rauth import OAuth2Service
import os
from fb import getFriends

app = Flask(__name__)
access_token = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/authenticate-facebook', methods=["GET"])
def authenticate_facebook():
    '''
    FB_CLIENT_ID = '769684356512385'
    FB_CLIENT_SECRET = 'bfafc3ab14067170a74e3977643584f6'
    graph_url = 'https://graph.facebook.com/'
    facebook = OAuth2Service(name='facebook',
        authorize_url='https://www.facebook.com/dialog/oauth',
        access_token_url=graph_url + 'oauth/access_token',
        client_id=app.config['FB_CLIENT_ID'],
        client_secret=app.config['FB_CLIENT_SECRET'],
        base_url=graph_url)
    redirect_url = url_for('authorized', _external=True)
    params = {'redirect_url': redirect_url}
    access_token = facebook.get_authorize_url(**params)
    '''
    return jsonify(success=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)