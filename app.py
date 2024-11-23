from flask import Flask, render_template, url_for
import firebase_admin
from firebase_admin import credentials
from flask_socketio import SocketIO, send, emit

cred = credentials.Certificate("firebase_voting.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)