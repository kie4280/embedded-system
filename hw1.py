from temp import Temp_sensor
import time
from push_button import Button
from pir import PIR_sensor
from led_control import LED
from buzzer import Buzzer
import threading
from event_listener import eventListener
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()


GPIO_PIR = 7
GPIO_BUTT = 19
GPIO_LED = 18
GPIO_BUZZ = 24
GPIO_TEMP = 4
TEMP_THRESH = 30

loop = True
e1 = eventListener(0.05)
e2 = eventListener(5)
pir = PIR_sensor(GPIO_PIR)
pir.initialize()
temp_s = Temp_sensor()
buzzer = Buzzer(GPIO_BUZZ)

times=0

def pirCallback():
    global times
    times+=1
    if(times>=3):
        buzzer.stop()
    print("motion")
    pass


def buttCallback(pressed):
    global L22
    
    print("pressed", pressed)
    if not pressed:
        L22 = e2.addListener(tempListener, tempCallback)


def tempListener():
    global L22, times
    cel, fer = temp_s.read_temp()
    print("read temp")
    if(cel != None and fer != None):
        if cel >= TEMP_THRESH:
            times = 0
            return True, {"cel": cel}
        else:
            return False, {"cel": None}
    else:
        return False, {"cel": None}

def tempCallback(cel):
    e2.removeListener(L22)
    buzzer.buzz(440)
    print("cel", cel)   


button = Button(GPIO_BUTT)
L11=e1.addListener(pir.getState, pirCallback)
L12=e1.addListener(button.getState, buttCallback)
L22=None


while loop:
    time.sleep(1)
