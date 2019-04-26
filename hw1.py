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
e1 = eventListener(0.01)
e2 = eventListener(0.01)
pir = PIR_sensor(GPIO_PIR)
pir.initialize()
temp_s = Temp_sensor()


def pirCallback():
    print("motion")
    pass


def buttCallback(pressed):
    print("pressed", pressed)


def tempListener():
    cel, fer = temp_s.read_temp()
    print("read temp")
    if(cel != None and fer != None and cel >= TEMP_THRESH):
        return True, {"cel": cel}
    else:
        return False, {"cel": None}

def tempCallback(cel):
    print("cel", cel)


button = Button(GPIO_BUTT)
e1.addListener(pir.getState, pirCallback)
e1.addListener(button.getState, buttCallback)
e2.addListener(tempListener, tempCallback)

while loop:
    time.sleep(1)
