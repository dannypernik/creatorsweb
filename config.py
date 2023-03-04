import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    XCAPTCHA_SITE_KEY = os.environ.get('HCAPTCHA_SITE_KEY')
    XCAPTCHA_SECRET_KEY = os.environ.get('HCAPTCHA_SECRET_KEY')
    XCAPTCHA_VERIFY_URL = os.environ.get('XCAPTCHA_VERIFY_URL')
    XCAPTCHA_API_URL = os.environ.get('XCAPTCHA_API_URL')
    XCAPTCHA_DIV_CLASS = os.environ.get('XCAPTCHA_DIV_CLASS')
    XCAPTCHA_THEME = os.environ.get('XCAPTCHA_THEME')
    MAILJET_KEY = os.environ.get('MAILJET_KEY')
    MAILJET_SECRET = os.environ.get('MAILJET_SECRET')
    ADMINS = [os.environ.get('ADMINS')]
    HELLO_EMAIL = os.environ.get('HELLO_EMAIL')
    PHONE = os.environ.get('PHONE')
