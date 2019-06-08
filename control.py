import RPi.GPIO as GPIO
from time import sleep

CONTROL_PIN = 14
CPIN = 15
SPIN = 2
PWM_FREQ = 50
STEP = 45
G1 = 20
G2 = 21

if __name__=="__main__":
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

GPIO.setup(CONTROL_PIN, GPIO.OUT)
GPIO.setup(CPIN, GPIO.OUT)
GPIO.setup(SPIN, GPIO.OUT)
GPIO.setup(G1, GPIO.IN)
GPIO.setup(G2, GPIO.IN)
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)
pwn = GPIO.PWM(CPIN, PWM_FREQ)
pwn.start(0)
pwo = GPIO.PWM(SPIN, PWM_FREQ)
pwo.start(0)


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading


def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle


def servo(yaw, pitch = 90):
    
    dc = angle_to_duty_cycle(pitch)
    pwm.ChangeDutyCycle(dc)
    dd = angle_to_duty_cycle(180-pitch)
    pwn.ChangeDutyCycle(dd)
    de = angle_to_duty_cycle(yaw)
    pwo.ChangeDutyCycle(de)    



# G3 =
# G4 =


# GPIO.setup(G3,GPIO.IN)
# GPIO.setup(G4,GPIO.IN)

