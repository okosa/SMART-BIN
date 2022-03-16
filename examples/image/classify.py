#!/usr/bin/env python
 
import device_patches       # Device specific patches for Jetson Nano (needs to be before importing cv2)
 
import cv2
import os
import sys, getopt
import signal
import time
import RPi.GPIO as GPIO
from motor_test import *
from motor import *
from send_sms import *

 
GPIO.setwarnings(False)

recycle = 3.5
metal = 5.8
compost = 8.2
other = 10.5
 
#GPIO pins for infrared
recycle_IR = 19
metal_IR = 5
compost_IR = 6
other_IR = 13

GPIO.setup(recycle_IR, GPIO.IN)
GPIO.setup(metal_IR, GPIO.IN)
GPIO.setup(compost_IR, GPIO.IN)
GPIO.setup(other_IR, GPIO.IN)

#go home
p.ChangeDutyCycle(other)
 
p.start(0) # Initialization
from edge_impulse_linux.image import ImageImpulseRunner
from gpiozero import LED
 
# led = LED(17)
 
runner = None
# if you don't want to see a camera preview, set this to False
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False
 
def now():
    return round(time.time() * 1000)
 
def get_webcams():
    port_ids = []
    for port in range(5):
        print("Looking for a camera in port %s:" %port)
        camera = cv2.VideoCapture(port)
        if camera.isOpened():
            ret = camera.read()[0]
            if ret:
                backendName =camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                print("Camera %s (%s x %s) found in port %s " %(backendName,h,w, port))
                port_ids.append(port)
            camera.release()
    return port_ids
 
def sigint_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)
 
signal.signal(signal.SIGINT, sigint_handler)
 
def help():
    print('python classify.py <path_to_model.eim> <Camera port ID, only required when more than 1 camera is present>')
 
def imageProcessing(again, argv):
    while again == 1:

        try:
            opts, args = getopt.getopt(argv, "h", ["--help"])
        except getopt.GetoptError:
            help()
            sys.exit(2)
     
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                help()
                sys.exit()
     
        if len(args) == 0:
            help()
            sys.exit(2)
     
        model = args[0]
     
        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, model)
     
        print('MODEL: ' + modelfile)
     
        with ImageImpulseRunner(modelfile) as runner:
            try:
                model_info = runner.init()
                print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
                labels = model_info['model_parameters']['labels']
                if len(args)>= 2:
                    videoCaptureDeviceId = int(args[1])
                else:
                    port_ids = get_webcams()
                    if len(port_ids) == 0:
                        raise Exception('Cannot find any webcams')
                    if len(args)<= 1 and len(port_ids)> 1:
                        raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use to this script")
                    videoCaptureDeviceId = int(port_ids[0])
     
                camera = cv2.VideoCapture(videoCaptureDeviceId)
                ret = camera.read()[0]
                if ret:
                    backendName = camera.getBackendName()
                    w = camera.get(3)
                    h = camera.get(4)
                    print("Camera %s (%s x %s) in port %s selected." %(backendName,h,w, videoCaptureDeviceId))
                    camera.release()
                else:
                    raise Exception("Couldn't initialize selected camera.")
     
                next_frame = 0 # limit to ~10 fps here
     
                for res, img in runner.classifier(videoCaptureDeviceId):
#                    
                    if (next_frame > now()):
                        time.sleep((next_frame - now()) / 1000)
     
                    # print('classification runner response', res)
                    Recycling = "Recycling"
                    Compost = "Compost"
                    Metal = "Metal"
                    acceptable_threshold = 0.8
                    if "classification" in res["result"].keys():
                        print('Result (%d ms.) ' % (res['timing']['dsp'] + res['timing']['classification']), end='')
                        for label in labels:
                           score = res['result']['classification'][label]
                           if score > acceptable_threshold and label == Recycling:
                                again = 0
                                return recycle
                           elif score > acceptable_threshold and label == Metal:
                                again = 0
                                return metal
                           elif score > acceptable_threshold and label == Compost:
                                again = 0
                                return compost
                           print('%s: %.2f\t' % (label, score), end='')
                        print('', flush=True)
     
                    elif "bounding_boxes" in res["result"].keys():
                        print('Found %d bounding boxes (%d ms.)' % (len(res["result"]["bounding_boxes"]), res['timing']['dsp'] + res['timing']['classification']))
                        for bb in res["result"]["bounding_boxes"]:
                            print('\t%s (%.2f): x=%d y=%d w=%d h=%d' % (bb['label'], bb['value'], bb['x'], bb['y'], bb['width'], bb['height']))
                            img = cv2.rectangle(img, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
     
                    if (show_camera):
                        cv2.imshow('edgeimpulse', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                        if cv2.waitKey(1) == ord('q'):
                            break
     
                    next_frame = now() + 100
            finally:
                if (runner):
                    runner.stop()
 
def IR(sensorPin):        
    i = GPIO.input(sensorPin)
    
    count = 0;

    while i == 0:
        count += 1
        time.sleep(1)
        if count >= 3:
            return True
        i = GPIO.input(sensorPin)

    return False


def identify2Pin(identify):
    
    if identify == 3.5:
        return 19
    if identify == 5.8:
        return 5
    if identify == 8.2:
        return 6
    if identify == 10.5:
        return 13
 

def main(argv):

    while True:
         
        isrecycleFull = IR(recycle_IR)      
        if isrecycleFull == True:
            send_text(recycle)
            
        ismetalFull = IR(metal_IR)      
        if ismetalFull == True:
            send_text(metal)
            
        iscompostFull = IR(compost_IR)      
        if iscompostFull == True:
            send_text(compost)
            
        isotherFull = IR(other_IR)      
        if isotherFull == True:
            send_text(other)
        
        #while infarred == False:
            
            #identify subsystem
            #again = 1
            #identify = imageProcessing(again, argv)
            #print("\nIdentify:", identify)
        
            #rotate to category
            #rotate(other, identify)
            
            #drop garbage
            #tray_open()
            #tray_close()
            
            #go home
            #rotate(identify, other)
            
            #check if bin is full
            #isBinFull = IR( identify2Pin(identify) )
                    
            #if isBinFull == True:
                #send_text(identify)
            
            

if __name__ == "__main__":
   main(sys.argv[1:])