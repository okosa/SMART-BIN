import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setwarnings(False)
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

recycle = 4.5  
metal = 6.5
compost = 8.3
other = 10
home = 4

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz


def rotate(previous, target):
    if previous < target:
        for i in np.arange (previous, target, 0.1):
            p.ChangeDutyCycle(i)
            time.sleep(0.04)
    else:
        for i in np.arange (previous, target, -0.1):
            p.ChangeDutyCycle(i)
            time.sleep(0.04)

