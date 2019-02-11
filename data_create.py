import cv2 as cv
import numpy as np
import os
import sys


def create_neg():
    for img in os.listdir("/neg/"):
        line = 'neg/'+img+'\n'
        with open('bg.txt','a') as f:
            f.write(line)


def create_pos():
    for img in os.listdir("/pos/"):
        line = 'pos/'+img+' 1 0 0 100 100\n' #!!maybe change the dimentions later!!
        with open('info.dat','a') as f:
            f.write(line)

#create_neg()
#create_pos()
