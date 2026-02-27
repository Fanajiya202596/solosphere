from flask import Blueprint, request, jsonify
from models.user import User

auth_bp = Blueprint("auth_bp", __name__)

# REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    created = User.create(username, password)

    if not created:
        return jsonify({"error": "Username already exists"}), 400

    return jsonify({"message": "User registered successfully"}), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user_id = User.authenticate(username, password)

    if not user_id:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user_id
    }), 200