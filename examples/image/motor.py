import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

recycle = 3.5
metal = 5.8
compost = 8.16
other = 10.5


p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5) # Initialization
try:
   while True:
    p.ChangeDutyCycle(other)
    time.sleep(2)
  
except KeyboardInterrupt:
  p.stop()
  #GPIO.cleanup()
  
finally:
    GPIO.cleanup()