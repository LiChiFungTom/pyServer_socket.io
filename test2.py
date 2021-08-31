from flask import Flask, render_template
from flask_socketio import SocketIO
import json




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def render_index():
    return render_template("index.html")

# player ball count

@app.route("/red")
def red():
    _data = json.dumps({ 'red' : 1, 'player' : 1 })
    socketio.emit('test',_data)
    return "red"

@app.route("/yellow")
def yellow():
    _data = json.dumps({ 'yellow' : 2, 'player' : 1})
    socketio.emit('test',_data)
    return "yellow"

@app.route("/blue")
def blue():
    _data = json.dumps({ 'blue' : 3, 'player' : 1 })
    socketio.emit('test',_data)
    return "blue"


# player 2 ball count

@app.route("/red2")
def red2():
    _data = json.dumps({ 'red2' : 1, 'player' : 2 })
    socketio.emit('test',_data)
    return "red2"

@app.route("/yellow2")
def yellow2():
    _data = json.dumps({ 'yellow2' : 2, 'player' : 2})
    socketio.emit('test',_data)
    return "yellow2"



@app.route("/blue2")
def blue2():
    _data = json.dumps({ 'blue2' : 3, 'player' : 2 })
    socketio.emit('test',_data)
    return "blue2"


# get client sned data
@socketio.on('zone')
def my_event(data):
    print('Received data: ', data)

if __name__ == '__main__':
    socketio.run(app,debug=True, host='0.0.0.0', port=4000 )