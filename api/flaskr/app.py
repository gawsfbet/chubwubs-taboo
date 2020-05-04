from flask import Flask
from flask_socketio import SocketIO

from .routes import core_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

app.register_blueprint(core_api)

if __name__ == '__main__':
    socketio.run(app)