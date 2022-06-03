from flask import Flask, jsonify
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "hello world"})

@app.route('/users', methods=['get'])
def usersHandler():
    return jsonify({"users": users})

app.run(host="0.0.0.0", port=4000, debug=True)