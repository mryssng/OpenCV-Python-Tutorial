#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * resize
    https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Read file
image = cv2.imread('images/Mandrill.jpg')

# Resize #1
h, w = image.shape[:2]
result = cv2.resize(image, (w * 2, h))
cv2.imwrite('images/resize_1.jpg', result)

# Resize #2
result = cv2.resize(image, None, fx=1, fy=2)
cv2.imwrite('images/resize_2.jpg', result)

# Comparing Interpolation Methods
# # Read file
image = cv2.imread('images/Mandrill.jpg')
h, w = image.shape[:2]
x_scale = 0.5
y_scale = 0.5

# INTER_NEAREST
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_NEAREST)
cv2.imwrite('images/resize_INTER_NEAREST.jpg', result)

# INTER_LINEAR
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('images/resize_INTER_LINEAR.jpg', result)

# INTER_CUBIC
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_CUBIC)
cv2.imwrite('images/resize_INTER_CUBIC.jpg', result)

# INTER_AREA
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_AREA)
cv2.imwrite('images/resize_INTER_AREA.jpg', result)

# INTER_LANCZOS4
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite('images/resize_INTER_LANCZOS4.jpg', result)

# INTER_LINEAR_EXACT
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_LINEAR_EXACT)
cv2.imwrite('images/resize_INTER_LINEAR_EXACT.jpg', result)

# INTER_NEAREST_EXACT
result = cv2.resize(image, None, fx=x_scale, fy=y_scale, interpolation=cv2.INTER_NEAREST_EXACT)
cv2.imwrite('images/resize_INTER_NEAREST_EXACT.jpg', result)

# # INTER_MAX
# result = cv2.resize(image, None, x_scale, y_scale, interpolation=cv2.INTER_MAX)
# cv2.imwrite('images/resize_INTER_MAX.jpg', result)

