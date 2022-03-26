import RPi.GPIO as GPIO
import time
import numpy as np
import pigpio

#GPIO.setwarnings(False)
servoPIN = 7
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)

recycle = 1000  
metal = 2000
compost = 1500
other = 500

#500  = 0 degrees
#1000 = 60
#1500 = 120
#2000 = 180

#p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz

p = pigpio.pi()
p.set_mode(servoPIN, pigpio.OUTPUT)
p.set_PWM_frequency(servoPIN, 50)
#go home
p.set_servo_pulsewidth(servoPIN, other)


def rotate(previous, target):
    if previous < target:
        for i in np.arange (previous, target, 10):
            p.set_servo_pulsewidth(servoPIN, i)
            time.sleep(0.04)
    else:
        for i in np.arange (previous, target, -10):
            p.set_servo_pulsewidth(servoPIN, i)
            time.sleep(0.04)
    


