from flask import Blueprint, request
from flask_jwt_extended import current_user, jwt_required
from extensions import db
from models import Task
from sqlalchemy import desc
from sockets import notify_task_creation


user_blp = Blueprint("user_blp", __name__)


# get all tasks
@user_blp.route("/get_tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    try:
        tasks = Task.query.filter_by(user_id=current_user.id
                                     ).order_by(desc(Task.date_created)).all()
        return {"tasks": [task.to_dict() for task in tasks]}, 200
    except Exception as e:
        print(e, "error@Get_tasks")
        return {"message": "Network Error"}, 500


@user_blp.route("/get_one_task/<task_id>", methods=["GET"])
@jwt_required()
def get_one_task(task_id):
    try:
        task = Task.query.filter_by(user_id=current_user.id,
                                     id=task_id).first()
        if not task:
            return {"message": "Task not found"}, 404
        return {"message": "Task found", "task": task.to_dict() }, 200
    except Exception as e:
        print(e, "error@Get_tasks")
        return {"message": "Network Error"}, 500


@user_blp.route("/create_task", methods=["POST"])
@jwt_required()
def create_task():
    try:
        data = request.get_json()

        title = data.get("title")
        task_content = data.get("content")

        if not title:
            return {"message": "Title is required"}, 400
        if not task_content:
            return {"message": "Task content is required"}, 400

        task = Task(
            title=title,
            task_content=task_content,
            user_id=current_user.id,
        )
        db.session.add(task)
        db.session.commit()
        notify_task_creation(task)
        return {"message": "Task created successfully"}, 201
    except Exception as e:
        print(e, "error@Create_task")
        db.session.rollback()
        return {"message": "Network Error"}, 500


# update task
@user_blp.route("/update_task/<task_id>", methods=["PATCH"])
@jwt_required()
def update_task(task_id):
    try:
        task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
        if not task:
            return {"message": "No task found"}, 404

        data = request.get_json()
        title = data.get("title")
        task_content = data.get("content")
        completed = data.get("completed") # This will be a boolean value (True/False)

        task.title = title if title else task.title
        task.task_content = task_content if task_content else task.task_content

        if completed and not isinstance(completed, bool):
            return {"message": "Invalid data type for completed"}, 400

        task.completed = completed if completed else task.completed

        db.session.commit()
        return {"message": "Task updated successfully"}, 200
    except Exception as e:
        print(e, "error@Update_task")
        db.session.rollback()
        return {"message": "Network Error"}, 500


# delete task
@user_blp.route("/delete_task/<task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    try:
        task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
        if not task:
            return {"message": "No task found"}, 404
        db.session.delete(task)
        db.session.commit()
        return {"message": "Task deleted successfully"}, 200
    except Exception as e:
        print(e, "error@Delete_task")
        db.session.rollback()
        return {"message": "Network Error"}, 500
