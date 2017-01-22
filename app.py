from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/authenticate-facebook', methods=["GET"])
def authenticate():

    return jsonify(success=True)

@app.route('/submit', methods=["POST"])
def submit():

    return jsonify(success=True, data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
