from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models.region import Region
from ..models.city import City
from ..extensions import db

city_controller = Blueprint('city', __name__)

@city_controller.get('/cities')
@city_controller.get('/cities/<int:region_id>')
@jwt_required()
def get_cities(region_id=None):
    if region_id is None:
        all_cities = City.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'region_id': c.region_id} for c in all_cities])

    region = Region.query.get(region_id)

    if not region:
        return jsonify({'error': 'Region not found'}), 404
    
    cities = City.query.filter(City.region_id == region_id).all()

    if cities:
        return jsonify([{'id': c.id, 'name': c.name, 'region_id': c.region_id} for c in cities])
    else:
        sub_regions = Region.query.filter(Region.parent_id == region_id).all()
        if sub_regions:
            return jsonify([{'id': r.id, 'name': r.name, 'parent_id': r.parent_id} for r in sub_regions])
        else:
            return jsonify({'message': 'No cities or sub-regions found for this region'}), 404

@city_controller.post('/city')
@jwt_required()
def add_city():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'region_id' not in data:
            return jsonify({"error": "Bad Request"}), 400
        
        if data['region_id'] is None:
            return jsonify({"error": "Bad Request"}), 400

        city = City(name = data['name'], region_id = data['region_id'])

        db.session.add(city)

        db.session.commit()

        return jsonify({'id': city.id, 'name': city.name, 'region_id': city.region_id}), 201
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

@city_controller.put('/city/<int:id>')
@jwt_required()
def update_city(id):
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
@jwt_required()
def delete_city(id):
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