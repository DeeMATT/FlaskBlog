import os

class Config:

    os.environ['EMAIL_USER'] = 'garyhelman1592@gmail.com'
    os.environ['EMAIL_PASSWORD'] = 'GODisable4000'

    SECRET_KEY = '803b9ff7a6dd470e4c3c68dfd0e1c81c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')