from extensions import db
import uuid
from passlib.hash import pbkdf2_sha256 as hasher
from datetime import datetime


def generate_id():
    return uuid.uuid4().hex


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(50), default=generate_id, primary_key=True, index=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    # relationship to task model
    tasks = db.relationship('Task', backref='user', lazy=True)

    @staticmethod
    def hash_password(password):
        return hasher.hash(password)

    @staticmethod
    def verify_password(password, hashed):
        return hasher.verify(password, hashed)

    # more password validation can be added here
    @staticmethod
    def password_validation(password):
        if len(password) < 8:
            return "Password should be at least 8 characters long"
        return None

    @staticmethod
    def username_exist(username):
        return User.query.filter_by(username=username).first()


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.String(50), default=generate_id, primary_key=True, index=True)
    title = db.Column(db.String(150), nullable=False)
    task_content = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)

    # serialized data to dict
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'task_content': self.task_content,
            'completed': self.completed,
            'date_created': self.date_created.strftime('%d-%b-%Y %H:%M:%S'),
        }
