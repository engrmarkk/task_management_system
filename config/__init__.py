import os
import json

base_dir = os.path.abspath(os.path.dirname(__file__))

database_uri = os.environ.get("DATABASE_URI",
                              f"sqlite:///{os.path.join(base_dir, 'task.sqlite')}")

if database_uri and database_uri.startswith("postgres://"):
    database_uri = database_uri.replace("postgres://", "postgresql://", 1)


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = database_uri
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "task.sqlite")
    JSON_SORT_KEYS = False
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


config_dict = {"development": DevelopmentConfig}
