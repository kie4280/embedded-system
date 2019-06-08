import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

def detect(a):
    while True:
        sum = 0
        signal = []
        for i in a:
            signal.append(GPIO.input(i))
        for i in signal:
            sum += i
        if sum == 1:
            for i in range(len(signal)):
                if signal[i] == 1:
                    return a[i]

try:
    while True:
        start_time = 0
        a = [4, 14, 15, 18]
        b = []
        time_diff = []

        sensor1 = detect(a)
        b.append(sensor1)
        for i in range(len(a)):
            if a[i] == sensor1:
                a.pop(i)
                break
        start_time = time.time()

        sensor2 = detect(a)
        b.append(sensor2)
        for i in range(len(a)):
            if a[i] == sensor2:
                a.pop(i)
                break
        end_time = time.time()
        time_diff.append(end_time - start_time)
        start_time = end_time

        sensor3 = detect(a)
        b.append(sensor3)
        for i in range(len(a)):
            if a[i] == sensor3:
                a.pop(i)
                break
        end_time = time.time()
        time_diff.append(end_time - start_time)
        start_time = end_time

        sensor4 = detect(a)
        b.append(sensor4)
        for i in range(len(a)):
            if a[i] == sensor4:
                a.pop(i)
                break
        end_time = time.time()
        time_diff.append(end_time - start_time)

        print(b)
        print(time_diff)
        time.sleep(0.3)


except KeyboardInterrupt:
    GPIO.cleanup()