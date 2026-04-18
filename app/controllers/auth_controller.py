from flask import Blueprint, jsonify, request
from ..models.user import User
from ..extensions import db;

auth_controller = Blueprint('auth', __name__)

@auth_controller.post('/register')
def register():
    try:
        data = request.get_json()

        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Bad Request"}), 400

        user = User(username = data['username'], password = data['password'])

        db.session.add(user)

        db.session.commit()

        return jsonify({'message': 'User was created'}), 201
    except:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500