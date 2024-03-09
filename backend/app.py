# backend/app.py
from flask import Flask, render_template, request, jsonify
from backend.database import db
from backend.models import Crop, Farm, Resource, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/update_crop', methods=['POST'])
def update_crop():
    data = request.get_json()
    crop = Crop.query.filter_by(id=data['id']).first()
    if crop:
        crop.soil_preparation_done = data['soil_preparation_done']
        crop.seeds_sowing_done = data['seeds_sowing_done']
        crop.irrigation_done = data['irrigation_done']
        crop.manure_pesticides_done = data['manure_pesticides_done']
        crop.harvesting_done = data['harvesting_done']
        crop.storage_done = data['storage_done']
        db.session.commit()
        return jsonify({'message': 'Crop updated successfully'})
    return jsonify({'message': 'Crop not found'})

@app.route('/update_farm', methods=['POST'])
def update_farm():
    data = request.get_json()
    farm = Farm.query.filter_by(id=data['id']).first()
    if farm:
        farm.cropped = data['cropped']
        db.session.commit()
        return jsonify({'message': 'Farm updated successfully'})
    return jsonify({'message': 'Farm not found'})

@app.route('/update_resource', methods=['POST'])
def update_resource():
    data = request.get_json()
    resource = Resource(name=data['name'], detail=data['detail'])
    db.session.add(resource)
    db.session.commit()
    return jsonify({'message': 'Resource added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
