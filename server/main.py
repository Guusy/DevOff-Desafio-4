from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

room = {

}

chat = []

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('connect_room')
def connect_room(nickname):
    room[request.sid] = { 'name': str(nickname) }
    socketio.emit('current_users', room, broadcast=True)

@socketio.on('send_message')
def send_message(message):
    chat.append( {'user': room[request.sid],  'message': message})
    socketio.emit('new_message_on_chat', chat, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)


