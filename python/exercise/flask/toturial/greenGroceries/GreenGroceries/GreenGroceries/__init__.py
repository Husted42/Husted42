import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

conn = psycopg2.connect(
    host="localhost",
    database=os.getenv('greenGroceries'),
    user=os.getenv('postgres'),
    password=os.getenv('password')
)

db_cursor = conn.cursor(cursor_factory=RealDictCursor)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from GreenGroceries import filters
from GreenGroceries.blueprints.Login.routes import Login
from GreenGroceries.blueprints.Produce.routes import Produce

app.register_blueprint(Login)
app.register_blueprint(Produce)
