import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print(" Button + GPIO ")
#while True:
 #    if ( GPIO.input(10) == False ):
  #        print("Button Pressed")
   #        os.system('date')
    #        print GPIO.input(10)
     #        time.sleep(5)
      #        else:
       #            os.system('clear')
        #            print (press the button..")
#       [2;2R[2;2[2;2R[2;2Rleep(1)
GPIO.setup(22,GPIO.OUT)

class Buzzer:

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def buzz_interval(self, interva):
        pass

def morsecode ():
#Dot Dot Dot
    GPIO.output(22,GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.1)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.2)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.2)

