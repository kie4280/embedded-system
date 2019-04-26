import os
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()

class Button:
    def __init__(self, pin):
        self.pin = pin
        self.statetime=-1
        self.prev_state=0
        GPIO.setup(pin, GPIO.IN)
    def getState(self):
        if self.statetime==-1:
            self.statetime = time.perf_counter()
        if (time.perf_counter()-self.statetime) > 0.05:
            return GPIO.input(self.pin)
        return 


while True:
    if (GPIO.input(10) == False):
        print ("button pressed")
        os.system("date")
        print(GPIO.input(10))
        time.sleep(5)
    else:
        os.system('clear')
        print("press the button..")
        time.sleep(1)