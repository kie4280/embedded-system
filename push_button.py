import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)
print(" Button + GPIO ")
print(GPIO.input(10))

while True:
    if (GPIO.input(10) == False):
        print "button pressed"
        os.system("date")
        print(GPIO.input(10))
        time.sleep(5)
    else:
        os.system('clear')
        print("press the button..")
        time.sleep(1)