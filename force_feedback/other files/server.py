#
#   server in Python
#   Binds REP socket to tcp://*:5555

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#
i = 1
num = 99000

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")
    num+=90
    #  Send reply back to client
    socket.send(bytes(str(num), 'utf8'))  #  copy this line to send response to client. i.e. the joystick force angle (where to pull to) and the force.
    if num >= 99360:
        num =99000
    time.sleep(5)