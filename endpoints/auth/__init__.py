from flask import Blueprint, request
from models import User, Task
from extensions import db
from flask_jwt_extended import current_user
from utils import return_access_token

auth_blp = Blueprint("auth", __name__)

@auth_blp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username:
            return {"message": "No username provided"}, 400
        if not password:
            return {"message": "No password provided"}, 400

        if User.username_exist(username):
            return {"message": "Username already exist"}, 400

        validation_message = User.password_validation(password)

        if validation_message:
            return {"message": validation_message}, 400
        hashed_password = User.hash_password(password)
        user = User(username=username.lower(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}, 201
    except Exception as e:
        print(e, "error@Register")
        db.session.rollback()
        return {"message": "Network Error"}, 500



# login
@auth_blp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username:
            return {"message": "Username is required"}, 400

        if not password:
            return {"message": "Password is required"}, 400

        user = User.username_exist(username)

        if not user:
            return {"message": "User does not exist"}, 400

        if not User.verify_password(password, user.password):
            return {"message": "Incorrect password"}, 400

        access_token = return_access_token(user)

        if not access_token:
            return {"message": "Something went wrong"}, 500

        return {"message": "Login successful", "access_token": access_token}, 200
    except Exception as e:
        print(e, "error@Login")
        return {"message": "Network Error"}, 500
