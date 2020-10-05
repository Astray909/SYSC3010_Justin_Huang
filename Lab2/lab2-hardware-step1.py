from sense_hat import SenseHat
import time

sense = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
X = (0,0,0)
P = (255,105, 180)

J = [
G,G,G,G,G,G,G,G,
G,G,G,G,G,G,G,G,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
X,X,X,G,G,X,X,X,
G,G,G,G,G,X,X,X,
G,G,G,G,G,X,X,X
]

H = [
P,P,P,X,X,P,P,P,
P,P,P,X,X,P,P,P,
P,P,P,X,X,P,P,P,
P,P,P,P,P,P,P,P,
P,P,P,P,P,P,P,P,
P,P,P,X,X,P,P,P,
P,P,P,X,X,P,P,P,
P,P,P,X,X,P,P,P
]

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

STATE = [J, H]
state = 0

while True:
    events = sense.stick.get_events()
    if events:
        for event in events:
            if event.action != 'pressed':
                continue
            if event.direction == 'left' or event.direction == 'right':
                sense.set_pixels(STATE[state])
                if state == 0:
                    state = 1
                elif state == 1:
                    state = 0
            if event.direction == 'up':
                state = 1
                sense.set_pixels(STATE[state])
            if event.direction == 'down' :
                sense.set_pixels(NONE)
            elif event.direction == 'middle':
                sense.set_pixels(NONE)
                exit()
