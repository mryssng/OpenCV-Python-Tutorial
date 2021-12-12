#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * split
    https://docs.opencv.org/4.5.2/d2/de8/group__core__array.html#ga0547c7fed86152d7e9d0096029c8518a
    
  * merge
    https://docs.opencv.org/4.5.4/d2/de8/group__core__array.html#ga7d7b4d6c6ee504b30a20b1680029c7b4

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Read file
image = cv2.imread('images/duck.jpg')

# Split
blue, green, red = cv2.split(image)
images = cv2.split(image)
cv2.imwrite('images/duck_blue.jpg', blue)
cv2.imwrite('images/duck_green.jpg', green)
cv2.imwrite('images/duck_red.jpg', red)

# Merge
image_grb = cv2.merge((green, red, blue))  # Order : green, red, blue
cv2.imwrite('images/duck_grb.jpg', image_grb)
