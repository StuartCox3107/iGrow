import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
  import env 


app = Flask(__name__)

app.config["DB_NAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo

# sets route so that index.html is main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# route to adding a record page
@app.route('/add_planting')
def add_planting():
    return render_template('create.html') 

# route to read page
@app.route('/read_planting')
def read_planting():
    return render_template('read.html') 

# route to update page
@app.route('/update_planting')
def update_planting():
    return render_template('update.html') 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)