from flask import Flask, render_template
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
  import env 


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


app = Flask(__name__)

mongo = PyMongo

@app.route('/')
def hello_world():
    return "Test"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)