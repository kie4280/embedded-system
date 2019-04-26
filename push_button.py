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
        # if self.statetime==-1:
        #     self.statetime = time.perf_counter()
        # if (time.perf_counter()-self.statetime) > 0.01:
        #     self.prev_state=GPIO.input(self.pin)
        #     self.statetime=time.perf_counter()
        #     return self.prev_state
        # else:
        #     pass
        
        butt_curr = GPIO.input(self.pin)
        # print("button", butt_curr)
        if self.prev_state != butt_curr:
            self.prev_state = butt_curr
            return True, {"pressed":butt_curr }
        
        return False, {"pressed":butt_curr }
