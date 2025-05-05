from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from routes.home import home
from routes.asistentes import asistentes
from routes.asistencias import asistencias
from routes.api import api
app = Flask(__name__)

app.config.from_object(Config)

# SQLAlchemy(app)

app.register_blueprint(home)
app.register_blueprint(asistentes)
app.register_blueprint(asistencias)
app.register_blueprint(api)