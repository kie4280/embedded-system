from event_listener import eventListener
import threading
from buzzer import Buzzer
from led_control import LED
from pir import PIR_sensor
from push_button import Button
from temp import temp_sensor
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()


GPIO_PIR=7
GPIO_BUTT=19
GPIO_LED=18
GPIO_BUZZ=24
GPIO_TEMP=4

def pirCallback():
    print("motion")
    pass

pir = PIR_sensor(GPIO_PIR)
pir.initialize()


e=eventListener(0.01)


e.addListener(pir.readState, pirCallback)