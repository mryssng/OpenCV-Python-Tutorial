#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * Show image : imshow

  * Image data : https://unsplash.com/photos/VTvnoNBowZs
'''

import cv2
import matplotlib.pyplot as plt


# Read file
image = cv2.imread('images/duck.jpg')

# Show image using OpneCV
cv2.imshow('Image-1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show image using OpneCV (improved)
cv2.namedWindow('Image-2', cv2.WINDOW_NORMAL)
cv2.imshow('Image-2', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show image using matplotlib
plt.imshow(image)
plt.show()

# Show image using matplotlib (improved)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image2)
plt.show()
