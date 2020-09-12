from flask import Flask, render_template
import os
from flask_pymongo import flask_PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
  import env 


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Test"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)