from flask import Flask, request, jsonify, make_response
from .models import Entry, entries

import json
import re

app = Flask(__name__)

#register route
@app.route('/register', methods=['POST'])
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

#login route
@app.route('/login', methods=['POST'])
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

#create entry route
@app.route("/api/v1/users/entries", methods=["POST"])
def create_entry():
    """ Endpoint to get the diary entry data entered by the user """
    # get request data
    entry_data = request.get_json()

    #check if entry data is not empty
    if not entry_data:
        return jsonify({"message":"Enter data in all fields"}), 400
    
    title = entry_data.get('title')
    date = entry_data.get('date')
    entryBody = entry_data.get('entryBody')
    entry_id = len(entries)+1

    # validate request data
    if not title or title == " " or title == type(int):
        return jsonify({'message': 'title is required'}), 400
    if not date or date == " ":
        return jsonify({'message': 'date is required'}), 400
    if not entryBody or entryBody == "":
        return jsonify({
            'status': 'Required',
            'message': 'Please write someting'}), 400

    new_entry = Entry(title, date, entryBody, entry_id)
    entries.append(new_entry)

    return jsonify({'message': 'You have successfully created your entry'}), 201

#route for fetiching all diary entries
@app.route("/api/v1/users/entries", methods=["GET"])
def fetch_entries():
    if len(entries) < 1:
        return jsonify({"status":"Fail",
            "Sorry":"You have no entries"
        }),404
    
    if len(entries) >= 1:
        return jsonify({
            "message":"Successfully fetched entries",
            "entriess":[
                entry.__dict__ for entry in entries
            ]
        }),200
    return jsonify({"Sorry":"Couldn\'t find any entries"}),400

#route for fetching single entry by id
@app.route('/api/v1/users/entries/<int:entry_id>', methods=['GET'])
def get_single_entry(entry_id):
    """ Endpoint to fetch a single entry """
    if len(entries) < 1:
        return jsonify({"status": "Fail",
                        "Sorry": "You have no entries"
                        }), 404
    for entry in entries:
        if entry.entry_id == entry_id:
            return jsonify({'entry': entry.__dict__}), 200
    return jsonify({'error': 'User Not Found'}), 404

#route for modifying an entry
@app.route("/api/v1/users/entries/<int:entry_id>", methods=['PUT'])
def modify_entry(entry_id):
    """ Endpoint to modify a given entry"""
    if len(entries) < 1:
        return jsonify({
            "status": "Fail",
            "Sorry": "You have no entries to modify"}), 404

    if len(entries) >= 1:
        entry_data = request.get_json()
        for entry in entries:
            if entry.entry_id == int(entry_id):
                title = entry_data.get('title')
                date = entry_data.get('date')
                entryBody = entry_data.get('entryBody')

                modified_entry = Entry(title, date, entryBody, entry_id)
                entries.insert(entry_id, modified_entry)
            return jsonify({
                "entry": entry.__dict__,
                "status": "OK",
                "Congratulations": "You successfully modified your entry"
            }), 201
