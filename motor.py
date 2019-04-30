from time import sleep
import RPi.GPIO as GPIO


DIR= 20  # Direction GPIO pin
STEP= 21 #Step GPIO pin
CW=1     #Clockwise Rotation
CCW=0    #Counterclockwise Rotation
SPR=200  #steps per revolution
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.output(DIR, CW)

step_count= SPR
delay=.0208


GPIO.output(14,GPIO.LOW)
for x in range (step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(2)
delay=delay/32
GPIO.output(14,GPIO.HIGH)
for x in range (step_count*16):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
  
    

##MODE= (14,15,18)

##RESOLUTION = {'Full': (0, 0, 0),
##              'Half': (1, 0, 0),
##              '1/4': (0, 1, 0),
##              '1/8': (1, 1, 0),
##              '1/16': (0, 0, 1),
##              '1/32': (1, 1, 1)}

##    
##GPIO.output(DIR, CW)
##for x in range (step_count):
##    GPIO.output(MODE, RESOLUTION['Half'])
##    sleep(delay)
##    GPIO.output(MODE, GPIO.LOW)
##    sleep(delay)
 
GPIO.cleanup()
m time import sleep
import RPi.GPIO as GPIO


DIR= 20  # Direction GPIO pin
STEP= 21 #Step GPIO pin
CW=1     #Clockwise Rotation
CCW=0    #Counterclockwise Rotation
SPR=200  #steps per revolution
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.output(DIR, CW)

step_count= SPR
delay=.0208


GPIO.output(14,GPIO.LOW)
for x in range (step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(2)
delay=delay/32
GPIO.output(14,GPIO.HIGH)
for x in range (step_count*16):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
  
    

##MODE= (14,15,18)

##RESOLUTION = {'Full': (0, 0, 0),
##              'Half': (1, 0, 0),
##              '1/4': (0, 1, 0),
##              '1/8': (1, 1, 0),
##              '1/16': (0, 0, 1),
##              '1/32': (1, 1, 1)}

##    
##GPIO.output(DIR, CW)
##for x in range (step_count):
##    GPIO.output(MODE, RESOLUTION['Half'])
##    sleep(delay)
##    GPIO.output(MODE, GPIO.LOW)
##    sleep(delay)
 
GPIO.cleanup()

