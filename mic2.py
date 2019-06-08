from event_listener import eventListener
import RPi.GPIO as GPIO
import time

mic_pins = [4,14,15,18]
order=list()
ts = list()
states=[1,1,1,1]
state_sums = [0, 0, 0, 0]
prev_time = 0

def callback(times, name):
    # print("sound collected")
    # print(times)
    order.append(name)
    if len(order) == 4:
        print(order)
        order.clear()

def scan0():
    
    global states, mic_pins, order, ts, prev_time, state_sums
    
    state = GPIO.input(mic_pins[0])
    if state == 0:
        return True, {"times":ts, "name":0}
    else :
        return False, {"times":ts, "name":0}

def scan1():
    
    global states, mic_pins, order, ts, prev_time, state_sums
    
    state = GPIO.input(mic_pins[1])
    if state == 0:
        return True, {"times":ts, "name":1}
    else :
        return False, {"times":ts, "name":1}

def scan2():
    
    global states, mic_pins, order, ts, prev_time, state_sums
    
    state = GPIO.input(mic_pins[2])
    if state == 0:
        return True, {"times":ts, "name":2}
    else :
        return False, {"times":ts, "name":2}
    
def scan3():
    
    global states, mic_pins, order, ts, prev_time, state_sums
    
    state = GPIO.input(mic_pins[3])
    if state == 0:
        return True, {"times":ts, "name":3}
    else :
        return False, {"times":ts, "name":3}

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    for i in mic_pins:
        GPIO.setup(i, GPIO.IN)

e0=eventListener(0)
e1=eventListener(0)
e2=eventListener(0)
e3=eventListener(0)
e0.addListener(scan0, callback)
e1.addListener(scan1, callback)
e2.addListener(scan2, callback)
e3.addListener(scan3, callback)

while True:
    # for a in range(4):
    #     state = GPIO.input(mic_pins[a])
    #     print("state", a, state)
    time.sleep(1)

