
class Config:
    """Configuracion base"""
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:alumno@localhost:3308/asistencia_sanitaria"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "12345678"