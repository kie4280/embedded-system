#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import threading

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)


def runThread():
    for b in LED.blink_list:

        pass
       

class LED:

    thread = threading.Thread(target=runThread, daemon=True)
    blink_list = []

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        LED.thread.start()

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def blink(self, interval, duration=0.5):
        self.led = (self.pin, interval, duration)
        LED.blink_list.append(self.led)

        pass

    def stop_blink(self):
        try:
            LED.blink_list.remove(self.led)
        except ValueError as e:
            pass

    
