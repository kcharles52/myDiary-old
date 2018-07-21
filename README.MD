# My diary
## [![Build Status](https://travis-ci.org/kcharles52/myDiary.svg?branch=api-travis)](https://travis-ci.org/kcharles52/myDiary) [![Coverage Status](https://coveralls.io/repos/github/kcharles52/myDiary/badge.svg?branch=api-travis)](https://coveralls.io/github/kcharles52/myDiary?branch=api-travis) [![Maintainability](https://api.codeclimate.com/v1/badges/51af961a3e2505aacc95/maintainability)](https://codeclimate.com/github/kcharles52/myDiary/maintainability)

This is an online application that helps users to record their memories

## Prerequisites
* Text editor
* Browser 
* Python/Flask framework

## Features
### User interface
* signup page
* signin page
* Diary entries
* Diary entry
* Add and modify entry
* Profile page
* Dashboard page

Preview on <a href="https://kcharles52.github.io/myDiary/UI/">Github pages</a>


### Built with
* HTML
* CSS
* javascript

### Endpoints 
HTTP Method|End point |Action
-----------|----------|--------------
POST | /api/v1/signup | Register a user
POST | /api/v1/login | Login a user
GET| /api/v1/entries   | Fetch all entries
GET | /api/v1/entry/<entry_Id> | Fetch a single entry
POST | /api/v1/entry | Create an entry
PUT | /api/v1/entries/<entry_id>/ | Modify entry

##  Technologies
* Python 3.6

## Testing frame
* nosetests
* pytest

##  How to setup the project
* Setup a virtual environment
* `pip install -r requirements.txt`

##  Run the application
* Run python3 run.py on command prompt
* View the api on http://127.0.0.1:5000/api/v1/register
* You can test the Endpoints with PostMan

## Author
[Kato Charles](https://github.com/kcharles52)
