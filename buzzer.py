import threading
import os
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()

class Buzzer(threading.Thread):
    def __init__(self, pin):
        self.isStop = False        
        GPIO.setup(pin,GPIO.OUT)
        self.pin = pin
        pass
    
    def beep(self, duration, freq):
        self.buzzer=GPIO.PWM(self.pin, freq)
        self.buzzer.start(50)
        self.timer = threading.Timer(duration, self.stop)
        self.timer.start()        
        pass

    
    def buzz(self, freq):
        self.buzzer=GPIO.PWM(self.pin, freq)
        self.buzzer.start(50)

    def stop(self):
        self.buzzer.stop()
        self.timer.cancel()
        pass

    def force_stop(self):
        self.stop()
        self.timer.cancel()
        pass

buzz = Buzzer(24)
buzz.beep(2, 440)
time.sleep(5)
buzz.beep(1, 880)
time.sleep(5)
buzz.stop()
