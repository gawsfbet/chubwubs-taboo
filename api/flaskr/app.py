import os
from flask import Flask

from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
    socketio.run(app)