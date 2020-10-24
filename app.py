"""Imports the relevant modules
Args:
    None
Returns:
    None.
"""
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["DB_NAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

"""Renders page for 404 error handling
Args:
    e: If 404 error triggered dur to page not found
Returns:
    The rendered 404.html page with button to return home.
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
    """Gets all records from database and paginates 6 records to
    display on the rendered landing page.
    Args:
        None
    Returns:
        The rendered index.html with 6 paginated records.
    """
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page = 6
    offset = (page -1) * per_page
    total = mongo.db.planting_records.find().count()
    planting_record = list(mongo.db.planting_records.find())
    paginated_records = planting_record[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materialize')
    return render_template('index.html',
                           plants=paginated_records,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/add_planting')
def add_planting():
    """Renders the page for creating a new record
    Args:
        None
    Returns: The rendered create.html page.
    """
    return render_template('create.html')

@app.route('/insert_planting', methods=['POST'])
def insert_planting():
    """Adds new record input to database
    Args:
        None
    Returns: The index.html page after adding the new record.
    """
    planting_records = mongo.db.planting_records
    planting_records.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route('/read_planting/<plant_id>')
def read_planting(plant_id):
    """Renders the details of the chosen plant
    Args:
        plant_id: The id of the chosen plant
    Returns:
        The rendered read.html.
    """
    return render_template('read.html',
    plant = mongo.db.planting_records.find_one(
        {'_id': ObjectId(plant_id)}))

@app.route('/edit_planting/<plant_id>')
def edit_planting(plant_id):
    """Renders the edit page with the chosen plant details populated
    Args:
        plant_id: The id of the chosen plant
    Returns:
        Returns the update.htmlpage.
    """
    the_plant =  mongo.db.planting_records.find_one({"_id": ObjectId(plant_id)})
    return render_template('update.html', plant=the_plant)


@app.route('/update_planting/<plant_id>', methods=['POST'])
def update_planting(plant_id):
    """Updates the record in the database with the new information
    Args:
        plant_id: The id of the plant
    Returns:
        The rendered index.html page.
    """
    plant = mongo.db.planting_records
    plant.update( {'_id': ObjectId(plant_id)},
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

@app.route('/delete_planting/<plant_id>')
def delete_planting(plant_id):
    """Deletes the chosen record from the database
    Args:
        plant_id: The id of the plant
    Returns: The rendered index.html page.
    """
    mongo.db.planting_records.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
