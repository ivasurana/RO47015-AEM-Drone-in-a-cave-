#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <math.h>
#include <linux/input.h>

static int ff_fd;
static struct ff_effect effect;

/* from 5 numbers from python to force percentage*/
int force(long input)
    {
    long local = input;
    while (local >= 100)
        {
            local /= 10;
        }
    return local;
    }


static void generate_force(long input)
{
    /*obtain force and angle from python parameter*/
    int angle = input %1000;
    int force_value = force(input);
    printf(" angle: %i and force_percentage: %i\n", angle, force_value);
    /* effect settings */
    effect.type = FF_CONSTANT;
    effect.u.constant.level = 0x7fff *force_value/99;//* force_value;
    effect.direction = 0xb6 * (angle); //angle in degrees
    printf("executed level: %i direction: %i \n", effect.u.constant.level, effect.direction);
    effect.u.constant.envelope.attack_length = 0;
    effect.u.constant.envelope.attack_level = 0;
    effect.u.constant.envelope.fade_length = 0;
    effect.u.constant.envelope.fade_level = 0;
    effect.trigger.button = 0;
    effect.trigger.interval = 0;
    effect.replay.length = 0xffff;
    effect.replay.delay = 0;
    static int first = 1;
    if (first) {
            effect.id = -1;
    }
    if (ioctl(ff_fd, EVIOCSFF, &effect) < 0) {
    /* If updates are sent to frequently, they can be refused */
    }
    /* start to play the effect */
    if (first) {
                struct input_event play;
                play.type = EV_FF;
                play.code = effect.id;
                play.value = 1;
                if (write(ff_fd, (const void*) &play, sizeof(play)) == -1) {
                    perror("Play effect");
                    exit(1);
        }
    }
    first = 0;
}

int main (int argc, char** argv)
{
    printf ("Connecting to game server...\n");
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
    zmq_connect (requester, "tcp://localhost:5555");
    const char * dev_name = argv[1];
    printf("connected device: %s ",dev_name);




    	/* Open force feedback device */
	ff_fd = open(dev_name, O_RDWR);
	if (ff_fd == -1) {
        perror("Open device file");
		exit(1);
	                   }
    while (1){   //main loop
        char buffer [32];
        zmq_send (requester, "give me number", 14, 0);
        zmq_recv(requester,buffer,32,0);

        /*from string to long */
        char *endptr;//, *str = buffer;
        long cijfer = strtol(buffer, &endptr, 10);

        generate_force(cijfer);
    }
zmq_close (requester);
zmq_ctx_destroy (context);
return 0;
}
