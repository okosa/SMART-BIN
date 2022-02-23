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

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5) # Initialization

def rotate(previous, target):
    if previous < target:
        for i in np.arange (previous, target, 0.1):
            p.ChangeDutyCycle(i)
            time.sleep(0.05)
    else:
        for i in np.arange (previous, target, -0.1):
            p.ChangeDutyCycle(i)
            time.sleep(0.05)

try:
    rotate(other, recycle)
    time.sleep(2)
    rotate(recycle, metal)
    time.sleep(2)
    rotate(metal, compost)
    time.sleep(2)
    rotate(compost, other)
    
except KeyboardInterrupt:
  p.stop()
  #GPIO.cleanup()
  
finally:
    GPIO.cleanup()