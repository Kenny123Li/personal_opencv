import cv2 as cv
import numpy as np
import os
import sys

path = "negatives/"
#path = "positives/"

folder = "neg/"
#folder = "pos/"

dirs = os.listdir(path)
num = 1

def gray_n_resize():
    for images in dirs:
        if os.path.isfile(path+images):
            img = cv.imread(path+images+'.jpg', cv.IMREAD_GRAYSCALE)
            res = cv.resize(img, (300,300))
            cv.imwrite(folder+str(num)+'.jpg', res)
            num += 1

gray_n_resize()
