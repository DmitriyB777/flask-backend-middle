from flask import Blueprint, jsonify
from ..models.city import City;

city_controller = Blueprint('city', __name__)

@city_controller.get('/cities')
def get_regions():
    cities = City.query.all()
    return jsonify({'name': 'hello get'})

@city_controller.post('/city')
def add_region():
    return jsonify({'name': 'hello post'})

@city_controller.put('/city')
def update_region():
    return jsonify({'name': 'hello put'})

@city_controller.delete('/city')
def delete_region():
    return jsonify({'name': 'hello delete'})