from event_listener import eventListener
import RPi.GPIO as GPIO
import time

mic_pins = [1,2,3,4]

def callback(times):
    print("sound collected")
    print(times)

def scan():

    order=list()
    ts = list()
    states=[0, 0, 0, 0]
    for a in range(4):
        state = GPIO.input(mic_pins[a])
        if state==1:
            print("sounded", a)
            order.append(a)
            states[a] = 1
            ts.append(time.clock())
    if(len(order)==4):
        print(order)
        return True, {"times":ts}
    else:
        return False, {}

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setup()
e=eventListener(0.01)
e.addListener(scan, callback)

while True:
    time.sleep(1)

