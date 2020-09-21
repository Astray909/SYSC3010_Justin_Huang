from sense_hat import SenseHat
import time
from random import choice
import random
from time import sleep

sense = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
X = (0,0,0)
P = (255,105, 180)

NONE = [
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X
]

arrow = [
X,X,X,W,W,X,X,X,
X,X,W,W,W,W,X,X,
X,W,X,W,W,X,W,X,
W,X,X,W,W,X,X,W,
X,X,X,W,W,X,X,X,
X,X,X,W,W,X,X,X,
X,X,X,W,W,X,X,X,
X,X,X,W,W,X,X,X
]

green_arrow = [
X,X,X,G,G,X,X,X,
X,X,G,G,G,G,X,X,
X,G,X,G,G,X,G,X,
G,X,X,G,G,X,X,G,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X
]

red_off = [
X,X,X,R,R,X,X,X,
X,X,X,R,R,X,X,X,
R,R,X,R,R,X,R,R,
R,R,X,R,R,X,R,R,
R,R,X,X,X,X,R,R,
R,R,X,X,X,X,R,R,
R,R,R,R,R,R,R,R,
R,R,R,R,R,R,R,R
]

#sense.show_message("Flick the joystick in the appropriate direction", scroll_speed=0.1, text_colour=[100,100,100])
pause = 3
play = True

STATE = ["humidity: ", "gyro: ", "pressure: ", "Temp: "]
state = 0

while play:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)
    events = sense.stick.get_events()
    if events:
        for event in events:
            if event.action != 'pressed':
                continue
            if event.direction == 'left':
                sense.set_rotation(270)
                sleep(0.5)
                sense.set_pixels(green_arrow)
                sleep(0.5)
                sense.set_rotation(0)
                sense.show_message(STATE[3], scroll_speed=0.05)
                msg = "%s" % (t)
                sense.show_message(msg, scroll_speed=0.05)
            elif event.direction == 'right':
                sense.set_rotation(90)
                sleep(0.5)
                sense.set_pixels(green_arrow)
                sleep(0.5)
                sense.set_rotation(0)
                sense.show_message(STATE[2], scroll_speed=0.05)
                msg = "%s" % (p)
                sense.show_message(msg, scroll_speed=0.05)
            elif event.direction == 'up':
                sense.set_rotation(0)
                sleep(0.5)
                sense.set_pixels(green_arrow)
                sleep(0.5)
                sense.set_rotation(0)
                sense.show_message(STATE[0], scroll_speed=0.05)
                msg = "%s" % (h)
                sense.show_message(msg, scroll_speed=0.05)
            elif event.direction == 'down':
                sense.set_rotation(180)
                sleep(0.5)
                sense.set_pixels(green_arrow)
                sleep(0.5)
                sense.set_rotation(0)
                sense.show_message(STATE[1], scroll_speed=0.05)
                msg = "%s, %s, %s" % (x, y, z)
                sense.show_message(msg, scroll_speed=0.05)
            elif event.direction == 'middle':
                sense.set_pixels(red_off)
                sleep(0.5)
                sense.set_pixels(NONE)
                exit()

    state = random.randint(0, 3)