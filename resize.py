#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * resize
    https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d

  * Image data : https://unsplash.com/photos/VTvnoNBowZs
'''

import cv2

# Read file
image = cv2.imread('images/duck.jpg')

# Resize #1
result = cv2.resize(image, None, fx=1, fy=2)
cv2.imwrite('images/resize_1.jpg', result)

# Resize #2
h, w = image.shape[:2]
result = cv2.resize(image, (w * 2, h))
cv2.imwrite('images/resize_2.jpg', result)