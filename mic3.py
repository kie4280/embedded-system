import RPi.GPIO as GPIO
import time

mic_pins = [14, 15, 18, 5]


def callback(pin):
    print("sound", pin)
    pass


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setup(mic_pins, GPIO.IN)
    
    GPIO.add_event_detect(5, GPIO.FALLING, callback=callback)  
    GPIO.add_event_detect(14, GPIO.FALLING, callback=callback)
    GPIO.add_event_detect(15, GPIO.FALLING, callback=callback)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=callback)

    while 1:
        time.sleep(1)
