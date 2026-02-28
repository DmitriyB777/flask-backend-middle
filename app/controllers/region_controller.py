from flask import Blueprint, jsonify

region_controller = Blueprint('region', __name__)

@region_controller.get('/regions')
def get_regions():
    return jsonify({'name': 'hello get'})

@region_controller.post('/region')
def add_region():
    return jsonify({'name': 'hello post'})

@region_controller.put('/region')
def update_region():
    return jsonify({'name': 'hello put'})

@region_controller.delete('/region')
def delete_region():
    return jsonify({'name': 'hello delete'})
