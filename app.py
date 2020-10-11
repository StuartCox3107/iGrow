# import modules needed

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from os import path

# for gitignore to hide sensitive information

if path.exists("env.py"):
  import env 

# creates instance of app

app = Flask(__name__)

# mongoDB config, env variables in env.py

app.config["DB_NAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

# sets route so that index.html is main page and displays entries
# working but needs pagination
@app.route('/')
@app.route('/index')
def index(): 
    return render_template('index.html',
    planting_records=mongo.db.planting_records.find())

# route to adding a record page
# working
@app.route('/add_planting')
def add_planting():
    return render_template('create.html') 

# to add new planting to database 
# working
@app.route('/insert_planting', methods=['POST'])
def insert_planting():
    planting_records = mongo.db.planting_records
    planting_records.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

# route to read page
# working
@app.route('/read_planting/<plant_id>')
def read_planting(plant_id):
    return render_template('read.html', 
    plant = mongo.db.planting_records.find_one(
        {'_id': ObjectId(plant_id)}))

@app.route('/update_planting/<plant_id>')
def edit_plant(plant_id):
    the_plant =  mongo.db.planting_records.find_one({"_id": ObjectId(plant_id)})
    return render_template('update.html', plant=the_plant)

# route to update page
@app.route('/update_planting/<plant_id>', methods=['POST'])
def update_planting(plant_id):
    plant = mongo.db.planting_records
    plant.update( {'id': ObjectId(plant_id) },
    {
        'date_planted':request.form.get('date_planted'),
        'plant_name':request.form.get('plant_name'),
        'plant_notes':request.form.get('plant_notes'),
        'grow_notes':request.form.get('grow_notes'),
        'harvest_date':request.form.get('harvest_date'),
        'harvest_notes':request.form.get('harvest_notes'),
        'grow_again':request.form.get('grow_again')
    })
    return redirect(url_for('index'))

# to delete plant and route to index
# working
@app.route('/delete_planting/<plant_id>')
def delete_planting(plant_id):
    mongo.db.planting_records.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)