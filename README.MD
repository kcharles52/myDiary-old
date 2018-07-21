# My diary

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


### BUilt with
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
