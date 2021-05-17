#
#   server in Python
#   Binds REP socket to tcp://*:5555

import time
import zmq
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#
i = 1
while True:


    #  Wait for next request from client
    message = socket.recv()    # copy this line to receive a 'dummy' message from force_feedback.C

    #########################
    print(f"Received request: {message}")
    i+=1
    time.sleep(1)
    #socket.send_string(str(i))  # send string
    num = 99000 + 360 * np.random.random()
    num = round(num)
    #######################################

    #  Send reply back to client
    socket.send(bytes(str(num), 'utf8'))  #  copy this line to send response to client. i.e. the joystick force angle (where to pull to) and the force.
