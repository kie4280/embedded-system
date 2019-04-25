import RPi.GPIO as GPIO
from time import sleep

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()

class PIR:
    def __init__(self, pin):
        self.Current_State = 0
        self.Previous_State = 0
        self.GPIO_PIR = pin        
        GPIO.setup(self.GPIO_PIR, GPIO.IN)

    def initialize(self):
        print "Waiting for PIR to settle ..."
        # Loop until PIR output is 0
        while GPIO.input(self.GPIO_PIR) == 1:
            self.Current_State = 0   

    def readState(self):
    
        # Read PIR state
        self.Current_State = GPIO.input(self.GPIO_PIR)
        if self.Current_State == 1 and self.Previous_State == 0:
        # PIR is triggered
            print "  Motion detected!"
                   # Record previous state            
            self.Previous_State = 1
            return True
        elif self.Current_State == 0 and self.Previous_State == 1:
            # PIR has returned to ready state
            print "  Ready"
            self.Previous_State = 0
            # Wait for 10 milliseconds
            sleep(0.01)
            return False
        
    
    # clean up gpio pins when we exit the script 
        pass
print "PIR Module Test (CTRL-C to exit)"  # Set pin as input
