from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

timer = 0 #this will be used to determine whether the pass is in the frame or not
boolean = True#this will help with determining the pass was in frame
              #long enough to be counted as the pass and not a random misfire

face_cascade = cv2.CascadeClassifier('cascade.xml')


camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
    if (timer > 30):#automatically stops once there is a positive reading
        break
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 10, 20, 3)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        boolean = False #so this does not accidentily subtract 1 from timer
        timer += 1
        print(timer)
        
    if (boolean):#if the pass is not in frame, then timer goes back to 0
        timer = 0
        
    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    rawCapture.seek(0)

    boolean = True#makes the computer check for the pass every time
    #or else it will reset the timer to 0
    
    if k == ord("q"):
        break

if (timer > 10):
    print("Successful")
else:
    print("Pass not detected")

cv2.destroyAllWindows()
