from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models.region import Region
from ..models.city import City
from ..extensions import db

region_controller = Blueprint('region', __name__)

@region_controller.get('/regions')
@jwt_required()
def get_regions():
    regions = Region.query.all()

    return jsonify([{'id': r.id, 'name': r.name, 'parent_id': r.parent_id} for r in regions])

@region_controller.post('/region')
@jwt_required()
def add_region():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'parent_id' not in data:
            return jsonify({"error": "Bad Request"}), 400

        region = Region(name = data['name'], parent_id = data['parent_id'])

        db.session.add(region)

        db.session.commit()

        return jsonify({'id': region.id, 'name': region.name, 'parent_id': region.parent_id}), 201
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

@region_controller.put('/region/<int:id>')
@jwt_required()
def update_region(id):
    try:
        region = db.session.get(Region, id)

        if not region:
            return jsonify({"error": "Not found"}), 404
    
        data = request.get_json()

        if not data:
            return jsonify({"error": "Bad Request"}), 400
        
        if 'name' in data:
            region.name = data['name']
        
        if 'parent_id' in data:
            region.parent_id = data['parent_id']
        
        db.session.commit()

        return jsonify({'id': region.id, 'name': region.name, 'parent_id': region.parent_id}), 200
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

@region_controller.delete('/region/<int:id>')
@jwt_required()
def delete_region(id):
    try:
        region = db.session.get(Region, id)

        if not region:
            return jsonify({"error": "Not found"}), 404

        regions_ids_to_remove = get_all_descendant_regions(region.id)

        cities_to_remove = City.query.filter(City.region_id.in_(regions_ids_to_remove)).all()

        for c in cities_to_remove:
            db.session.delete(c)
        
        regions_to_remove_objects = Region.query.filter(Region.id.in_(regions_ids_to_remove)).all()
        for r in regions_to_remove_objects:
            db.session.delete(r)

        db.session.commit()

        return jsonify({'message': 'The item was successfully deleted'}), 200
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

def get_all_descendant_regions(region_id):
    descendant_regions_ids = set()
    regions_to_process = [region_id]

    while regions_to_process:
        current_region_id = regions_to_process.pop()
        descendant_regions_ids.add(current_region_id)

        subregions = Region.query.filter_by(parent_id=current_region_id).all()
        for subregion in subregions:
            regions_to_process.append(subregion.id)
            
    return list(descendant_regions_ids)
