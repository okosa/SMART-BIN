#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

in1 = 17
in2 = 18
en = 23

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
p = GPIO.PWM(en, 50)
Duty_cycle = 30
p.start(2.5)


while 1:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            p.ChangeDutyCycle(Duty_cycle)
            time.sleep(2)
            
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            p.ChangeDutyCycle(Duty_cycle )
            time.sleep(2)
            
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            p.ChangeDutyCycle(Duty_cycle )
            time.sleep(2)
            
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            p.ChangeDutyCycle(Duty_cycle )
            time.sleep(2)
            
            
        
   