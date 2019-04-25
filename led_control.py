#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import threading

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)

class LED:

    thread = threading.Thread(target=runThread)
    def __init__(self, pin):
        self.pin=pin
        GPIO.setup(pin, GPIO.OUT)
    def on(self):
        GPIO.output(18, GPIO.HIGH)
    def off(self):
        GPIO.output(18, GPIO.LOW)
    def blink(self, interval, duration=0.5):
        thread = 0
        pass
    def runThread(self):
        pass

        