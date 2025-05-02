from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from routes.home import home
from routes.asistentes import asistentes

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

app.register_blueprint(home)
app.register_blueprint(asistentes)