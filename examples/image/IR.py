#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

IR_out = 24

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_out, GPIO.IN)

while True:
    if GPIO.input(IR_out) == False:
        print("detected")
    else:
        print("undetected")