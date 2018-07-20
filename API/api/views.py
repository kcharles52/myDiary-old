from flask import Flask, request, jsonify, make_response

import json
import re

app = Flask(__name__)

#register route


@app.route('/api/v1/users/register', methods=['POST'])
def register_user():
    #get user data from request
    user_data = request.get_json()

    #check if data has been passed into URL
    if not user_data:
        return jsonify({'message': 'All fields are required'}), 400

    name = user_data['name']
    email = user_data['email']
    password = user_data['password']

    if not name or name == " " or name == type(int) or len(name) < 3:
        return jsonify({'message': 'Invalid name'}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status": "Fail",
            "message": "Enter valid email"}), 400)
    if not password or password == " " or len(password) < 5:
        return jsonify({'message': 'A stronger password  is required'}), 400

    return jsonify({'message': 'User {} has been registered'.format(name)}), 201


@app.route('/api/v1/users/login', methods=['POST'])
def login_user():
    # getting user data
    user_data = request.get_json()

    #check if returned user data is empty
    if not user_data:
        return jsonify({'Missing': 'These fields are required'}), 400

    email = str(user_data.get('email')).strip()
    password = user_data.get('password')


    if not email or email ==" ":
        return jsonify({'Missing': 'email is required'}), 400

    if not password or password ==" ":
        return jsonify({'Missing': 'password  is required'}), 400
    return jsonify({"message": "Welcome. You are logged in"}),200
