import os

class Config:
    SECRET_KEY = 'chave-secreta'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
