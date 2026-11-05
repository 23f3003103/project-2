from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    data = {
        'message': "Hello World"
    }
    return jsonify(data), 200


@app.route('/api/add/<int:a>/<int:b>', methods=['GET'])
def add(a,b):
    result = a + b
    data = {
        'value': result,
        'message': f"Addition of two numbers {a} and {b} is {result}"
    }
    return jsonify(data), 200

@app.route('/api/multiplication', methods=['GET'])
def multiplication():
    request_data = request.get_json()
    result_data = {
        'value': request_data['a'] * request_data['b'],
        'message': f"Multiplication of two numbers {request_data['a']} and {request_data['b']} is {request_data['a'] * request_data['b']}"

    }
    return jsonify(result_data), 200






if __name__ == "__main__":
    app.run(debug = True)


