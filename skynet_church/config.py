import os


class Config():
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    THUMBNAIL_SIZE = 256
    UPLOAD_PATH = 'uploads'