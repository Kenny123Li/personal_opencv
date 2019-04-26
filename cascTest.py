from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import numpy as np
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 15
ORDER = neopixel.RGBW
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

timer = 0 #track time
boolean = True  #controls loop
o = 2 #track pixels


#cascade file in same location
pass_cascade = cv2.CascadeClassifier('cascade.xml')

#setup camera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
    if (timer > 30): #stops loop if continuously positive for 3 seconds
        print ("Okay")
        pixels.fill((255,0,0,0))
        pixels.show()
        
        break

    #running the cascade
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = pass_cascade.detectMultiScale(gray, 9, 40, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        boolean = False
        timer += 1
        if (timer%2==0): #AS TIME PASSES, THE STRIP WILL GAIN BLUE PIXELS UNTIL A RED OR GREEN RING IS SHOWN
            pixels[o]=(0,0,255,0)
            pixels.show()
            o+=1

    if (boolean):#if the pass is not in frame, then timer goes back to 0
        timer = 0
        o=0
        pixels.fill((0,255,0,0))
        pixels.show()
        time.sleep(1)
        o=0
        
    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    rawCapture.seek(0)

    boolean = True#makes the computer check for the pass every time
    #or else it will reset the timer to 0
    
    if k == ord("q"):
        break

cv2.destroyAllWindows()
