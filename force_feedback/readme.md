# force feedback controller

python should send the force and angle to the C program. send it as 1 number. e.g. 99180 is force 99 and 180 degrees.

## in the python file:
```python
   import zmq
```
define connection:
```python
   context = zmq.Context()
   socket = context.socket(zmq.REP)
   socket.bind("tcp://*:5555")
```
receive request: (python waits for reply)
```python
message = socket.recv() 
```
send reply: (send force/angle) number = 99180 means force 99 (maximum) and angle 180 degrees
```python
socket.send(bytes(str(number), 'utf8')) 
```
## The C-file
compile C-file:
```
gcc -Wall -g force_joystick.c -lzmq -o force_joystick
 ```
 run:
```
./force_joystick /dev/input/by-id/usb-*event-joystick
```

## Procedure
first start the C program. It waits for the python file to start. for smooth control send high frequency commands. (10hz+)

