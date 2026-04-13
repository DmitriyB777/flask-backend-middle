from flask import Blueprint, jsonify, request
from ..models.city import City;
from ..extensions import db;

city_controller = Blueprint('city', __name__)

@city_controller.get('/cities')
def get_regions():
    cities = City.query.all()

    return jsonify([{'id': c.id, 'name': c.name, 'region_id': c.region_id} for c in cities])

@city_controller.post('/city')
def add_region():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'region_id' not in data:
            return jsonify({"error": "Bad Request"}), 400

        city = City(name = data['name'], region_id = data['region_id'])

        db.session.add(city)

        db.session.commit()

        return jsonify({'id': city.id, 'name': city.name, 'region_id': city.region_id}), 201
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

@city_controller.put('/city/<int:id>')
def update_region(id):
    try:
        city = db.session.get(City, id)

        if not city:
            return jsonify({"error": "Not found"}), 404
    
        data = request.get_json()

        if not data:
            return jsonify({"error": "Bad Request"}), 400
        
        if 'name' in data:
            city.name = data['name']
        
        if 'region_id' in data:
            city.region_id = data['region_id']
        
        db.session.commit()

        return jsonify({'id': city.id, 'name': city.name, 'region_id': city.region_id}), 200
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

@city_controller.delete('/city/<int:id>')
def delete_region(id):
    try:
        city = db.session.get(City, id)

        if not city:
            return jsonify({"error": "Not found"}), 404
        
        db.session.delete(city)

        db.session.commit()

        return jsonify({'message': 'The item was successfully deleted'}), 200
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500