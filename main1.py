import RPi.GPIO as GPIO
import time
from time import sleep
import control
from event_listener import eventListener

CONTROL_PIN = 14
CPIN = 15
SPIN = 2
PWM_FREQ = 50
STEP = 45

if __name__=="__main__":
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)


G1 = 20
G2 = 21
# G3 =
# G4 =

GPIO.setup(G1, GPIO.IN)
GPIO.setup(G2, GPIO.IN)
# GPIO.setup(G3,GPIO.IN)
# GPIO.setup(G4,GPIO.IN)


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading


def response(degree):
    control.servo(degree)

prev_state = (0,0)
def red():

    global prev_state
    state = (GPIO.input(G1), GPIO.input(G2))
    if state == prev_state:
        return False

    prev_state = state
    if state == (0,1):
        print('G2')
        return True, {"degree":0}
        
    elif state == (1, 0):
        print('G1')
        return True, {"degree":90}
        
    elif state == (1, 1):
        print('G1&G2')
        return True, {"degree":45}
        
    else:
        print('NO NO')
        return True, {"degree":180}
        



i = 0
print('a')
#x = RCtime(26)
x = 40
print('b')
print(x)
print('c')

pir_listener = eventListener(0.2)
pir_listener.addListener(red, response)
while True:
    sleep(1)
    if x > 30:
        
        i += 1
        # print(i)
