from functools import wraps
from flask import Flask, request
from models.db import db, People

db.create_tables([People])

app = Flask(__name__)

@app.route("/people", methods=["GET", "POST"])
def create_readall_people():
    p = People()
    if request.method == "GET":
        return [i for i in p.select().dicts()], 200
    elif request.method == "POST":
        p.name = request.get_json().get("name")
        p.save()
        return {}, 201
    else:
        return 405   

@app.route("/people/<id>")
def update_delete_read_people(id):
    if request.method == "PATCH":
        pass
    elif request.method == "GET":
        pass
    elif request.method == "DELETE":
        pass
    else:
        return 405
    
    
