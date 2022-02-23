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
        p.ChangeDutyCycle(recycle)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+0.2)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+0.4)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+0.6)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+0.8)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+1.0)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+1.2)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+1.4)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+1.6)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+1.8)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+2.0)
        time.sleep(1)
        p.ChangeDutyCycle(recycle+2.2)
        time.sleep(1)
        
        p.ChangeDutyCycle(metal)
        time.sleep(1)
        p.ChangeDutyCycle(metal+0.2)
        time.sleep(1)
        p.ChangeDutyCycle(metal+0.4)
        time.sleep(1)
        p.ChangeDutyCycle(metal+0.6)
        time.sleep(1)
        p.ChangeDutyCycle(metal+0.8)
        time.sleep(1)
        p.ChangeDutyCycle(metal+1.0)
        time.sleep(1)
        p.ChangeDutyCycle(metal+1.2)
        time.sleep(1)
        p.ChangeDutyCycle(metal+1.4)
        time.sleep(1)
        p.ChangeDutyCycle(metal+1.6)
        time.sleep(1)
        p.ChangeDutyCycle(metal+1.8)
        time.sleep(1)
        p.ChangeDutyCycle(metal+2.0)
        time.sleep(1)
        p.ChangeDutyCycle(metal+2.2)
        time.sleep(1)
        
        p.ChangeDutyCycle(compost)
        time.sleep(1)
        p.ChangeDutyCycle(compost+0.2)
        time.sleep(1)
        p.ChangeDutyCycle(compost+0.4)
        time.sleep(1)
        p.ChangeDutyCycle(compost+0.6)
        time.sleep(1)
        p.ChangeDutyCycle(compost+0.8)
        time.sleep(1)
        p.ChangeDutyCycle(compost+1.0)
        time.sleep(1)
        p.ChangeDutyCycle(compost+1.2)
        time.sleep(1)
        p.ChangeDutyCycle(compost+1.4)
        time.sleep(1)
        p.ChangeDutyCycle(compost+1.6)
        time.sleep(1)
        p.ChangeDutyCycle(compost+1.8)
        time.sleep(1)
        p.ChangeDutyCycle(compost+2.0)
        time.sleep(1)
        p.ChangeDutyCycle(compost+2.2)
        time.sleep(1)
        
        p.ChangeDutyCycle(other)
        time.sleep(1)
        p.ChangeDutyCycle(other+0.2)
        time.sleep(1)
        p.ChangeDutyCycle(other+0.4)
        time.sleep(1)
        p.ChangeDutyCycle(other+0.6)
        time.sleep(1)
        p.ChangeDutyCycle(other+0.8)
        time.sleep(1)
        p.ChangeDutyCycle(other+1.0)
        time.sleep(1)
        p.ChangeDutyCycle(other+1.2)
        time.sleep(1)
        p.ChangeDutyCycle(other+1.4)
        time.sleep(1)
        p.ChangeDutyCycle(other+1.6)
        time.sleep(1)
        p.ChangeDutyCycle(other+1.8)
        time.sleep(1)
        p.ChangeDutyCycle(other+2.0)
        time.sleep(1)
        p.ChangeDutyCycle(other+2.2)
        time.sleep(1)
    
   
        
    
except KeyboardInterrupt:
  p.stop()
  #GPIO.cleanup()
  
finally:
    GPIO.cleanup()