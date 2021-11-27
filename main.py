from config import PORT, HOST, DEBUG
from __init__ import app
from util.Ma import ma
from util.Db import db

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host=HOST, port=PORT, debug=bool(DEBUG))
