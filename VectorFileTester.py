from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascade.xml')

camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    rawCapture.seek(0)
    
    if k == ord("q"):
        break


cv2.destroyAllWindows()
