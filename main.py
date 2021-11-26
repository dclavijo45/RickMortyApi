from __init__ import app
from config import PORT, HOST, DEBUG

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=bool(DEBUG))
