from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from routes.home import home

app = Flask(__name__, static_folder="static", template_folder="templates")

app.config.from_object(Config)

db = SQLAlchemy(app)

app.register_blueprint(home)