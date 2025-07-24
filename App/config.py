import os
from dotenv import load_dotenv

load_dotenv()

# Explicitly specify the path to .env
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    LOGIN_MESSAGE = os.getenv('LOGIN_MESSAGE')
    LOGIN_MESSAGE_CATEGORY = os.getenv('LOGIN_MESSAGE_CATEGORY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
