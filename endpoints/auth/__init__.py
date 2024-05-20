from flask import Blueprint, request, jsonify
from models import User, Task
from extensions import db
from utils import return_access_token

auth_blp = Blueprint("auth", __name__)

@auth_blp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username:
            return jsonify({"message": "No username provided"}), 400
        if not password:
            return {"message": "No password provided"}, 400

        if User.username_exist(username):
            return jsonify({"message": "Username already exist"}), 400

        validation_message = User.password_validation(password)

        if validation_message:
            return jsonify({"message": validation_message}), 400
        hashed_password = User.hash_password(password)
        user = User(username=username.lower(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        print(e, "error@Register")
        db.session.rollback()
        return jsonify({"message": "Network Error"}), 500



# login
@auth_blp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username:
            return jsonify({"message": "Username is required"}), 400

        if not password:
            return jsonify({"message": "Password is required"}), 400

        user = User.username_exist(username)

        if not user:
            return jsonify({"message": "User does not exist"}), 400

        if not User.verify_password(password, user.password):
            return jsonify({"message": "Incorrect password"}), 400

        access_token = return_access_token(user)

        if not access_token:
            return jsonify({"message": "Something went wrong"}), 500

        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    except Exception as e:
        print(e, "error@Login")
        return jsonify({"message": "Network Error"}), 500
