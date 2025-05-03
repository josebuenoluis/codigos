from app import app
from models.db import db

with app.app_context():
    db.init_app(app)
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8000)