from flask import Flask,redirect,url_for
from flask_login import LoginManager,login_user,logout_user,login_required
from config import Config
from flask_sqlalchemy import SQLAlchemy
from services import mariadb_service as db_service
from routes.home import home
from routes.asistentes import asistentes
from routes.asistencias import asistencias
from routes.api import api
from routes.login import login
app = Flask(__name__)

app.config.from_object(Config)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id:int):
    return db_service.getUser(id)

def status_401(error):
    return redirect(url_for("login.iniciar_sesion"))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>",404

# SQLAlchemy(app)

app.register_blueprint(home)
app.register_blueprint(asistentes)
app.register_blueprint(asistencias)
app.register_blueprint(api)
app.register_blueprint(login)
app.register_error_handler(401,status_401)
app.register_error_handler(404,status_404)