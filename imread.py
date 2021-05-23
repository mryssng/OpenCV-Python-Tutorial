#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * Load image : imread
  https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

  * Image data : https://unsplash.com/photos/VTvnoNBowZs
'''

import cv2

# Read file without imread flag
image1 = cv2.imread('images/duck.jpg')
cv2.imwrite('images/duck_out.jpg', image1)

# Read file without imread flag
image2 = cv2.imread('images/duck.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('images/duck_gray.jpg', image2)

# When the image file can't be read, imread returns "None".
image3 = cv2.imread('images/_duck.jpg')

# Example to check if image is being read
image4 = cv2.imread('images/duck.jpg')
if image4 is not None:
    print('Image file was read.')
else:
    print('Image file was NOT read.')
