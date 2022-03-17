#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

in1 = 17
in2 = 22
en = 23

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
q = GPIO.PWM(en, 50)
Duty_cycle = 30
q.start(2.5)

def tray_close():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    q.ChangeDutyCycle(Duty_cycle)
    time.sleep(2)

def tray_open():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    q.ChangeDutyCycle(Duty_cycle )
    time.sleep(2)
    
