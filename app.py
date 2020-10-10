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

mongo = PyMongo(app)

# sets route so that index.html is main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', planting_records=mongo.db.planting_records.find())

# route to adding a record page
@app.route('/add_planting')
def add_planting():
    return render_template('create.html') 

# to add new planting to database 
@app.route('/insert_planting', methods=['POST'])
def insert_planting():
    planting_records = mongo.db.planting_records
    planting_records.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

# route to read page
@app.route('/read_planting')
def read_planting():
    return render_template('read.html') 

# route to update page
@app.route('/update_planting')
def update_planting():
    return render_template('update.html') 

# to delete plant and route to index
@app.route('/delete_planting/<plant_id>')
def delete_planting(plant_id):
    mongo.db.planting_records.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)