# AEM_drone_in_cave
This repository is part of the experiment 'tele-operated virtual drone in cave'. In this experiment force feedback is tested. To test force feedback a Microsoft force feedback joystick is used. the experiment consist of 2 files (one python file and one C file).
The files communicate via ZMQ protocol. In the C-file force commands are sended to the joystick which are received from the python file. the python file uses pygame to simulate the cave and the drone. the python also reads out the position of the joystick to calculate the dynamics of the drone.

##The C-file
compile C-file:
gcc -Wall -g force_joystick.c -lzmq -o force_joystick
run:
./force_joystick /dev/input/by-id/usb-*event-joystick

#Procedure
first start the C program. It waits for the python file to start. for smooth control send high frequency commands. (10hz+)
